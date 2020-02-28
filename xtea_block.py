# -*- coding: utf-8 -*-
"""
Created on Thu Nov 3 12:27:37 2016

@author: Dejan
"""

def xtea_encrypt(data,key): # data is of type Int; key is of type list of ints (1x4); return is int
    v0=data>>32
    v1=data&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(key[0])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(2654435769+key[3])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(2654435769+key[1])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(1013904242+key[2])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(1013904242+key[2])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(3668340011+key[1])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(3668340011+key[3])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(2027808484+key[0])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(2027808484+key[0])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(387276957+key[0])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(387276957+key[1])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(3041712726+key[3])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(3041712726+key[2])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(1401181199+key[2])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(1401181199+key[3])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(4055616968+key[1])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(4055616968+key[0])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(2415085441+key[0])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(2415085441+key[1])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(774553914+key[0])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(774553914+key[2])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(3428989683+key[3])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(3428989683+key[3])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(1788458156+key[2])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(1788458156+key[0])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(147926629+key[1])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(147926629+key[1])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(2802362398+key[1])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(2802362398+key[2])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(1161830871+key[0])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(1161830871+key[3])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(3816266640+key[3])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(3816266640+key[0])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(2175735113+key[2])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(2175735113+key[1])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(535203586+key[1])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(535203586+key[2])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(3189639355+key[1])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(3189639355+key[3])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(1549107828+key[0])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(1549107828+key[0])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(4203543597+key[3])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(4203543597+key[1])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(2563012070+key[2])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(2563012070+key[2])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(922480543+key[1])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(922480543+key[3])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(3576916312+key[1])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(3576916312+key[0])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(1936384785+key[0])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(1936384785+key[1])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(295853258+key[3])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(295853258+key[2])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(2950289027+key[2])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(2950289027+key[3])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(1309757500+key[2])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(1309757500+key[0])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(3964193269+key[1])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(3964193269+key[1])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(2323661742+key[0])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(2323661742+key[2])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(683130215+key[3])))&0xFFFFFFFF
    v0 = (v0+(((v1<<4^v1>>5)+v1)^(683130215+key[3])))&0xFFFFFFFF
    v1 = (v1+(((v0<<4^v0>>5)+v0)^(3337565984+key[2])))&0xFFFFFFFF
    
    return((v0<<32)+v1)
    
def xtea_decrypt(data,key):
    v0 = data>>32
    v1 = data&0xFFFFFFFF
    
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(3337565984+key[2])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(683130215+key[3])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(683130215+key[3])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(2323661742+key[2])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(2323661742+key[0])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(3964193269+key[1])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(3964193269+key[1])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(1309757500+key[0])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(1309757500+key[2])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(2950289027+key[3])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(2950289027+key[2])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(295853258+key[2])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(295853258+key[3])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(1936384785+key[1])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(1936384785+key[0])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(3576916312+key[0])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(3576916312+key[1])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(922480543+key[3])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(922480543+key[1])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(2563012070+key[2])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(2563012070+key[2])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(4203543597+key[1])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(4203543597+key[3])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(1549107828+key[0])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(1549107828+key[0])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(3189639355+key[3])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(3189639355+key[1])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(535203586+key[2])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(535203586+key[1])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(2175735113+key[1])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(2175735113+key[2])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(3816266640+key[0])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(3816266640+key[3])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(1161830871+key[3])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(1161830871+key[0])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(2802362398+key[2])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(2802362398+key[1])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(147926629+key[1])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(147926629+key[1])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(1788458156+key[0])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(1788458156+key[2])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(3428989683+key[3])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(3428989683+key[3])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(774553914+key[2])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(774553914+key[0])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(2415085441+key[1])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(2415085441+key[0])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(4055616968+key[0])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(4055616968+key[1])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(1401181199+key[3])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(1401181199+key[2])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(3041712726+key[2])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(3041712726+key[3])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(387276957+key[1])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(387276957+key[0])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(2027808484+key[0])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(2027808484+key[0])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(3668340011+key[3])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(3668340011+key[1])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(1013904242+key[2])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(1013904242+key[2])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(2654435769+key[1])))&0xFFFFFFFF
    v1 = (v1-(((v0<<4^v0>>5)+v0)^(2654435769+key[3])))&0xFFFFFFFF
    v0 = (v0-(((v1<<4^v1>>5)+v1)^(key[0])))&0xFFFFFFFF
      
    return((v0<<32)+v1)

    
    
    

    
#data=b'ovdetek8'
#key=b'treba16karaktera'
#data=int.from_bytes(data,'big')    
#key=[int.from_bytes(key[4*x:(x+1)*4],'big') for x in range(4)]
#    
#print(data==xtea_decrypt(xtea_encrypt(data,key),key))

#suma = (delta * 32) & mask
#mask=0xFFFFFFFF
#delta=0x9e3779b9
#v0=data_e>>32
#v1=data_e&0xFFFFFFFF
#for round in range(32):
#    v1 = (v1 - (((v0<<4 ^ v0>>5) + v0) ^ (suma + key[suma>>11 & 3]))) & mask
#    suma = (suma - delta) & mask
#    v0 = (v0 - (((v1<<4 ^ v1>>5) + v1) ^ (suma + key[suma & 3]))) & mask
#    rez=((v0<<32)+v1)