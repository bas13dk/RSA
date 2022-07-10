import gmpy2

def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


p = 404796306518120759733507156677
q = 404796306518120759733507156677
e = 65537
c = 150635433712900935381157860417761227624682377134647578768653

n=p*q
phi=(p-1)*(q-1)
d = gmpy2.invert(e, phi)
m = pow(c,d,n)

print(int_to_bytes(int(m)))



