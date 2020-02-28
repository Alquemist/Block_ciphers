# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 12:27:37 2016

@author: Dejan
"""
import time
import itertools

mask=0xFFFFFFFF
#idx_l=[0,1,2,3]*16 #v0
#idx_d=[3,2,1,0,0]*2+[3,2,1,1,0]*3+[3,2,2,1,0,3,2] #v1

def xtea(data,key): # data is of type Intiger; key is of type list of ints (1x4)
    v0=data[0]
    v1=data[1]
#    v0=data>>32
#    v1=data&0xFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(key[0])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(2654435769+key[3])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(2654435769+key[1])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(1013904242+key[2])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(1013904242+key[2])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(3668340011+key[1])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(3668340011+key[3])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(2027808484+key[0])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(2027808484+key[0])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(387276957+key[0])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(387276957+key[1])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(3041712726+key[3])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(3041712726+key[2])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(1401181199+key[2])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(1401181199+key[3])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(4055616968+key[1])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(4055616968+key[0])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(2415085441+key[0])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(2415085441+key[1])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(774553914+key[0])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(774553914+key[2])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(3428989683+key[3])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(3428989683+key[3])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(1788458156+key[2])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(1788458156+key[0])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(147926629+key[1])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(147926629+key[1])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(2802362398+key[1])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(2802362398+key[2])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(1161830871+key[0])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(1161830871+key[3])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(3816266640+key[3])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(3816266640+key[0])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(2175735113+key[2])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(2175735113+key[1])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(535203586+key[1])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(535203586+key[2])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(3189639355+key[1])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(3189639355+key[3])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(1549107828+key[0])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(1549107828+key[0])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(4203543597+key[3])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(4203543597+key[1])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(2563012070+key[2])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(2563012070+key[2])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(922480543+key[1])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(922480543+key[3])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(3576916312+key[1])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(3576916312+key[0])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(1936384785+key[0])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(1936384785+key[1])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(295853258+key[3])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(295853258+key[2])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(2950289027+key[2])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(2950289027+key[3])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(1309757500+key[2])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(1309757500+key[0])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(3964193269+key[1])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(3964193269+key[1])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(2323661742+key[0])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(2323661742+key[2])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(683130215+key[3])))&0xFFFFFFFF
    v0 =(v0+(((v1<<4^v1>>5)+v1)^(683130215+key[3])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(3337565984+key[2])))&0xFFFFFFFF
#    return((v0<<32)+v1)
#    print(v0,v1)
    
def xteaRef(data,key):
    s=0
    v0=data1[0]
    v1=data1[1]
    for i in range(32):
        idx_l=s&3
        v0 =(v0+(((v1<<4^v1>>5)+v1)^(s+key[idx_l])))&mask
        s=(s+delta)&mask;
        idx_d=(s>>11)&3
        v1 = (v1+(((v0<<4^v0>>5)+v0)^(s+key[idx_d])))&mask
#    print(v0,v1)


delta=0x9E3779B9
data1=[0xAF20A390, 0x547571AA]
data=(0xAF20A390<<32)+0x547571AA
key=[0x27F917B1, 0xC1DA8993, 0x60E2ACAA, 0xA6EB923D ]



times=10**5
t_start=time.process_time()
for _ in itertools.repeat(None, times):
    c=xtea(data1,key)
t_end=time.process_time()-t_start

t_start=time.process_time()
for _ in itertools.repeat(None, times):
    xteaRef(data,key)
t_end1=time.process_time()-t_start
print(t_end/times)
print(t_end1/times)