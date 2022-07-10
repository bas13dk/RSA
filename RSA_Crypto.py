from Crypto.Util.number import getPrime
from random import randrange

def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

p = getPrime(randrange(10,100))
q = getPrime(randrange(10,100))
n = p * q
e = 65537
c = 150635433712900935381157860417761227624682377134647578768653

phi =(p-1)*(q-1)

def inv(x, M):
    u = (x, 1)
    v = (M, 0)
    while v[0] != 0:
        q = u[0] // v[0]
        t = (u[0] % v[0], u[1] - q * v[1])
        u = v
        v = t
    if u[0] != 1: return 0
    return u[1] % M

d = inv (e,phi)

M = pow(c,d,n)

qwe = d*e
k = qwe%n

print(int(k))