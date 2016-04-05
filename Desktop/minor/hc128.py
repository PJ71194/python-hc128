import base64
from pbkd import PBKD
from byte import Byte

def hex_to_bit(x):
   return 

def bit_to_hex(h):
   return

def rotl(x,n):
   return ((x << n)^(x >> (32 − n))

def rotr(x,n):
   return ((x >> n)^(x << (32−n))

def f1(x):
   return rotr(x,7)^rotr(x,18)^(x >> 3)

def f2(x):
   return rotr(x,17)^rotr(x,19)^(x >> 10)

def g1(x, y, z):
   return (rotr(x,10)^rotr(z,23)) + rotr(y,8)

def g2(x, y, z):
   return (rotl(x,10)^rotl(z,23)) + rotl(y,8)

def h1(x):
   return Q[x0] + Q[256 + x2]

def h2(x):
   return P[x0] + P[256 + x2]

def init(K,IV):
    for i in range(0,4):
	temp1 = K[i*4:i*4+4]
	temp2 = IV[i*4:i*4+4]	
	K = K+temp1
	IV = IV+temp2
    for i in range(0,8):
	W = W + K[i*4:i*4+4]
    for i in range(8,16):
	W = W + IV[(i-8)*4:(i-8)*4+4]	
    for i in range(16,1280):
        W = W + f2(W[(i-2)*4:(i-2)*4+4]) + W[(i-7)*4:(i-7)*4+4] + f1(W[(i-15)*4:(i-15)*4+4]) + W[(i-16)*4:(i-16)*4+4] + i 
    for i in range(0,512):
	P = P + W[(i+256)*4:(i+256)*4+4]
	Q = Q + W[(i+768)*4:(i+768)*4+4]    

    for i in range(0,512):

        

