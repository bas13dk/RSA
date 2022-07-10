from Crypto.Util.number import getPrime
from random import randrange
from Crypto.Util.number import GCD
from Crypto.Util.number import inverse

p = getPrime(10)
q = getPrime(10)
n = p * q

phi = (p-1)*(q-1)

for e in range(2, phi):
    if GCD(e, phi) == 1:
        break

d = inverse(e, phi)
result = f"""
    p: {p}
    q: {q}
    n: {n}
    phi: {phi}
    e: {e}
    d: {d}
    """
print(result)

for i in range(10):
    m = randrange(1, n)
    c = pow(m, d, n)
    m2 = pow(c, e, n)

    result = f"""
   {m}   |   {c}   |   {m2}
   """

    print(result)
