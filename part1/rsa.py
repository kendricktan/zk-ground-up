"""
2019-01-06 Kendrick Tan
RSA

Rivest–Shamir–Adleman (RSA) is a process that allows
two parties to exchange secret information within
each other over an insecure line (e.g. the internet)

Party A sends Party B it's public key.
Party B uses the public key to encrypt the message they want to send
Party A receives encrypted message, decrypts it using their private key
"""

def gcd(a, b):
    """
    Greatest Common Divisor
    """
    m = min(a, b)

    for i in range(m, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

    return 1

def xgcd(a, b):
    """
    Extended Euclidean Distance

    return (g, x, y) such that a*x + b*y = g = gcd(x, y)
    """
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

def encrypt(msg, e, n):
    return ''.join([chr(ord(c)**e % n) for c in msg])

def decrypt(msg, d, n):
    return ''.join([chr(ord(c)**d % n) for c in msg])

# 1. Choose two distinct prime numbers p and q
p = 23
q = 31

# 2. Calculate n = p*q
n = p*q

# 3. Calculate the totient: phi(n) = (p - 1)*(q - 1)
phi_n = (p - 1) * (q - 1)

# 4.1 Choose integer e such that 1 < e < phi_n
e = 7
assert 1 < e < phi_n

# 4.2 Assert greatest-common-divisor (gcd) between e and phi_n = 1
# i.e. e and phi_n share no factors other than 1
assert gcd(e, phi_n) == 1

# 5. Compure d to satisgy the congruence relation d * e = 1 mod phi_n
# i.e. de = 1 + k * phi_n

# goal is to find d such that e*d = 1 mod phi_n
# EED calculates x and y such that ax + by = gcd(a, b)
# Let a = e, b = phi_n, therefore:
# gcd(e, phi_n) = 1 
# is equal to
# e*x + phi_n*y = 1
# take mod phi_n
# (e*x + phi_ny*y) mod phi_n = 1 mod phi_n
# = e*x = 1 mod phi_n
_, d, _ = xgcd(e, phi_n)

assert (d * e % phi_n) == 1

# 6. Encrypt a message using the public key (e)
# c = m**e % n
orig_msg = 'hello world'
enc_msg = encrypt(orig_msg, e, n)

# 7. Decrypt number using the private key (d)
# m = c**e % n
dec_msg = decrypt(enc_msg, d, n)

assert orig_msg == dec_msg

print(f'original message: {orig_msg}')
print(f'encrypted message: {enc_msg}')
print(f'decrypted message: {dec_msg}')

"""
This works because we know that:

d*e = 1 mod phi_n
d*e = k*phi_n + 1

c = m**e mod n
m = c**d mod n (sub c)
  = (m**e mod n)**d mod n
  = m**(d * e) mod n
  = m**(k*phi_n + 1) mod n
  = (m**(phi_n)**k)*m**1 mod n # note: m^(phi_n) = 1 mod n
  = (1 mod n)**k * m**1 mod n
  = 1**k * m**1 mod n
  = m mod n

https://crypto.stackexchange.com/questions/1789/why-is-rsa-encryption-key-based-on-modulo-varphin-rather-than-modulo-n
"""