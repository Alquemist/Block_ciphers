# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 12:22:31 2016

@author: dejan
Serpent Bitslice mode (4 Threads)
"""

from threading import Thread

Ptxt=b'treba16karaktera' #Plaintext
Ptxt=int.from_bytes(Ptxt,'big') #154784425670732647129557059640532234849
uKey=[0xFEDCBA98, 0xFEDCBA97, 0xFEDCBA96, 0xFEDCBA95, 0xFEDCBA94, 0xFEDCBA97, 0xFEDCBA92, 0xFEDCBA91] #256 bits
delta=0x9E3779B9
Sbox = [
	[ 3, 8,15, 1,10, 6, 5,11,14,13, 4, 2, 7, 0, 9,12 ], # S0
	[15,12, 2, 7, 9, 0, 5,10, 1,11,14, 8, 6,13, 3, 4 ], # S1
	[ 8, 6, 7, 9, 3,12,10,15,13, 1,14, 4, 0,11, 5, 2 ], # S2
	[ 0,15,11, 8,12, 9, 6, 3,13, 1, 2, 4,10, 7, 5,14 ], # S3
	[ 1,15, 8, 3,12, 0,11, 6, 2, 5, 4,10, 9,14, 7,13 ], # S4
	[15, 5, 2,11, 4,10, 9,12, 0, 3,14, 8,13, 6, 7, 1 ], # S5
	[ 7, 2,12, 5, 8, 4, 6,11,14, 9, 1,15,13, 3,10, 0 ], # S6
	[ 1,13,15, 0,14, 8, 2,11, 7, 4,12,10, 9, 3, 5, 6 ], # S7
    ]

SBox_Inv = [
    [13, 3, 11, 0, 10, 6, 5, 12, 1, 14, 4, 7, 15, 9, 8, 2],
    [5, 8, 2, 14, 15, 6, 12, 3, 11, 4, 7, 9, 1, 13, 10, 0],
    [12, 9, 15, 4, 11, 14, 1, 2, 0, 3, 6, 13, 5, 8, 10, 7],
    [0, 9, 10, 7, 11, 14, 6, 13, 3, 5, 12, 2, 4, 8, 15, 1],
    [5, 0, 8, 3, 10, 9, 7, 14, 2, 12, 11, 6, 4, 15, 13, 1],
    [8, 15, 2, 9, 4, 1, 13, 14, 11, 6, 5, 3, 7, 12, 10, 0],
    [15, 10, 1, 13, 5, 3, 6, 0, 4, 9, 14, 7, 2, 12, 8, 11],
    [3, 0, 6, 13, 9, 14, 15, 8, 5, 12, 11, 7, 10, 1, 4, 2]
    ]

IPTable = [
    0, 32, 64, 96, 1, 33, 65, 97, 2, 34, 66, 98, 3, 35, 67, 99,
    4, 36, 68, 100, 5, 37, 69, 101, 6, 38, 70, 102, 7, 39, 71, 103,
    8, 40, 72, 104, 9, 41, 73, 105, 10, 42, 74, 106, 11, 43, 75, 107,
    12, 44, 76, 108, 13, 45, 77, 109, 14, 46, 78, 110, 15, 47, 79, 111,
    16, 48, 80, 112, 17, 49, 81, 113, 18, 50, 82, 114, 19, 51, 83, 115,
    20, 52, 84, 116, 21, 53, 85, 117, 22, 54, 86, 118, 23, 55, 87, 119,
    24, 56, 88, 120, 25, 57, 89, 121, 26, 58, 90, 122, 27, 59, 91, 123,
    28, 60, 92, 124, 29, 61, 93, 125, 30, 62, 94, 126, 31, 63, 95, 127,
    ]
FPTable = [
    0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60,
    64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104, 108, 112, 116, 120, 124,
    1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61,
    65, 69, 73, 77, 81, 85, 89, 93, 97, 101, 105, 109, 113, 117, 121, 125,
    2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62,
    66, 70, 74, 78, 82, 86, 90, 94, 98, 102, 106, 110, 114, 118, 122, 126,
    3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63,
    67, 71, 75, 79, 83, 87, 91, 95, 99, 103, 107, 111, 115, 119, 123, 127,
    ]

    
def bit_rotate(num, places, l):
    '''places>0 => rol (Big endian)''' 
    '''places<0 => ror (Big endian)'''

    places=places%l
    num_s=((num&(2**(l-places)-1))<<places)+(num>>(l-places))
    return(num_s)
    
def S(nBox,inp): 
    return Sbox[nBox%8][inp]
    
def S_bsl(inp,x,r,S_out): #S Bitslice, parallel version of S
    q_out=(Sbox[r%8][(inp>>124-x&8)+(inp>>93-x&4)+(inp>>62-x&2)+(inp>>31-x&1)])
    S_out[0][x]=(q_out>>3)<<31-x
    S_out[1][x]=(q_out>>2&1)<<31-x
    S_out[2][x]=(q_out>>1&1)<<31-x
    S_out[3][x]=(q_out&1)<<31-x

def Lt(X): #Bitslice
    X[0]=bit_rotate(X[0], 13, 32)
    X[2]=bit_rotate(X[2], 3, 32)
    X[1]=X[1]^X[0]^X[2]
    X[3]=X[3]^X[2]^X[0]>>3
    X[1]=bit_rotate(X[1], 1, 32)
    X[3]=bit_rotate(X[3], 7, 32)
    X[0]=X[0]^X[1]^X[3]
    X[2]=X[2]^X[3]^X[1]>>7
    X[0]=bit_rotate(X[0], 5, 32)
    X[2]=bit_rotate(X[2], 22, 32)
    return(sum(
               [X[0]<<96,X[1]<<64,X[2]<<32,X[3]]
               ))
    
def PBox(PTable,inp): #PTable is permutation table, type list of ints; inp is of type int
    #Permutate bits acording to PTable
    #Assumes inp has len(PTable) number of bits
    res=0
    for i in range(len(PTable)):
        res=(res<<1)+(inp>>(127-PTable[i])&1)
    return(res)


def Serpent_encrypt(Ctxt):
    for r in range(31):
        S_out=[{},{},{},{}]
        Ctxt = Ctxt^K[r]
        for x in range(32): #32
            t=Thread(target=S_bsl,args=(Ctxt,x,r,S_out,), daemon='True')
            t.start()
        Ctxt=Lt(
               [sum(S_out[0].values()), sum(S_out[1].values()),
                sum(S_out[2].values()), sum(S_out[3].values())]
                )
    r+=1
    S_out=[{},{},{},{}]
    Ctxt = Ctxt^K[r]
    for x in range(32):
        t=Thread(target=S_bsl,args=(Ctxt,x,r,S_out,), daemon='True')
        t.start()
    return (c,sum(
                [sum(S_out[0].values())<<96, sum(S_out[1].values())<<64,
                 sum(S_out[2].values())<<32, sum(S_out[3].values())]
                 )^K[32])
    
            
def makeSubkeys(uKey):
    k_int={}
    for i in range(-8,0):
        k_int[i]=uKey[i]
    for i in range(132):
        k_int[i]=bit_rotate(
        (k_int[i-8]^k_int[i-5]^k_int[i-3]^k_int[i-1]^delta^i),
        11,32)
    
    k=[0]*132
    for i in range(33):
        nBox=(35-i)%32
        for j in range(32):
            inp=(((k_int[4*i]>>(31-j))&1)<<3)+(((k_int[1+4*i]>>(31-j))&1)<<2)+\
                (((k_int[2+4*i]>>(31-j))&1)<<1)+((k_int[3+4*i]>>(31-j))&1)
            out=S(nBox,inp)

            k[4*i]=(k[4*i]<<1)+(out>>3)
            k[1+4*i]=(k[1+4*i]<<1)+(out>>2&1)
            k[2+4*i]=(k[2+4*i]<<1)+(out>>1&1)
            k[3+4*i]=(k[3+4*i]<<1)+(out&1)

    K=[0]*33
    K2=[0]*33
    for i in range(33):
         K[i]=((k[4*i]<<96) + (k[4*i+1]<<64) + (k[4*i+2]<<32) + k[4*i+3])
         K2[i]=PBox(IPTable,K[i])
    
    return(K, K2)
    
K, Khat=makeSubkeys(uKey) # 851363545

c,Ctxt = Serpent_encrypt(Ptxt)



#c=[0]*32
#for r in range(32):
#    Ptxt = Rfn(r, Ptxt)
#    c[r]=Ptxt

#time.sleep(1)
#Ptxtint('final'+str(threading.active_count()))
    

#ak=[bin(x) for x in a]
#bkhat=ak=[bin(x) for x in b]


          
def getnth_bit(num,n):
    return((num>>n)&1)
