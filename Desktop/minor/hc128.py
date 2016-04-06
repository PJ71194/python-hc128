import base64
from pbkd import PBKD
from byte import Byte

def hex_to_bit(x):
   return 

def bit_to_hex(h):
   return

def mod(x):
   return x % 512

def substr(s,i):
   return s[i*4:i*4+4]

def update_substr(s,i,r):
   return s[:,i] + r + s[i*4+4,:]

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
	temp1 = substr(K,i)
	temp2 = substr(IV,i)	
	K = K+temp1
	IV = IV+temp2
    for i in range(0,8):
	W = W + substr(K,i)
    for i in range(8,16):
	W = W + substr(IV,i-8)
    for i in range(16,1280):
        W = W + f2(substr(W,i-2)) + substr(W,i-7) + f1(substr(W,i-15)) + substr(W,i-16) + i 
    for i in range(0,512):
	P = P + substr(W,i+256)
	Q = Q + substr(W,i+768)   

    for i in range(0,512):
	r = (substr(P,i) + g1(substr(P,mod(i-3)),substr(P,mod(i-10)),substr(P,mod(i-511))) ^ h1(substr(P,mod(i-12)))
	P = update_substr(P,i,r)

    for i in range(0,512):
	r = (substr(Q,i) + g2(substr(Q,mod(i-3)),substr(Q,mod(i-10)),substr(Q,mod(i-511))) ^ h2(substr(Q,mod(i-12)))
	Q = update_substr(Q,i,r)

	

        

