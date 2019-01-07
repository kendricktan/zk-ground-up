"""
2019-01-06 Kendrick Tan
Diffie-Hellman

Diffie-Hellman is a process that allows two parties to
generate a unique secret key _together_ while exchanging
information in plain text.

This script is purely for educational purposes only.
"""

# 1. We need to first establish our generator (g) and
# base (p) (both of which are arbitrarily large prime numbers)
p = 7
g = 11

# 2. Alice creates a secret key with a random value
secret_a = 8

# 3. Alice generates a public key from the secret key using
# the following formula: public = g^secret mod p
public_a = g**secret_a % p

# 4. Bob does the same thing
secret_b = 4
public_b = g**secret_b % p

# 5. Alice sends her public key to Bob, and Bob does the same thing
# Alice and Bob will now generate the shared secret key using
# the following formula: shared_secret = public^secret mod p

shared_secret_alice = public_b**secret_a % p
shared_secret_bob   = public_a**secret_b % p

# 6. Both of the generated shared secrets should contain the same value
if shared_secret_alice == shared_secret_bob:
    print('Shared secret generation successful!')
else:
    print('Shared secret generation failed :(')

"""
This works because of math :-)

Recall:
Exponent rule: (g^a)^b = g^(a*b)
Modulus rule: (g^a mod p)^b mod p = g^(a*b) mod p

So,

public_a = g^secret_a mod p

shared_secret_bob   = public_a^secret_b mod p
                    = (g^secret_a mod p)^secret_b mod p
                    = g^(secret_a * secret_b) mod p

shared_secret_alice = public_b^secret_a mod p
                    = (g^secret_b mod p)^secret_a mod p
                    = g^(secret_b * secret_a) mod p

"""