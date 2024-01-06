"""
To find the private key 'd' in an RSA encryption system, you'll need the following:

1) Two distinct prime numbers: 'p' and 'q'.
2) Public exponent 'e'.
3) Encrypted message 'c'.

Firstly, you'll need to calculate the modulus 'n' using the provided prime numbers 'p' and 'q': (to decrypt message in the end)
n=p×q

Then, compute Euler's totient function of 'n' using the prime factors 'p' and 'q':  (to get the private key)
ϕ(n)=(p−1)×(q−1)

The Euler's Totient Function counts the numbers lesser than a number say n that do not share any 
common positive factor other than 1 with n or in other words are co-prime with n. Hence, there are 
4 numbers(1,3,5 and 7) that are lesser than 8 and are co-prime with it.

1 and 8 are co-prime as the only common factor is 1 itself
2 and 8 have a common factor 2
3 and 8 are co-prime
4 and 8 have a common factor 2
5 and 8 are co-prime
6 and 8 have a common factor 2
7 and 8 are co-prime
8 and 8 have a common factor 2
Hence, there are 4 numbers(1,3,5 and 7) that are lesser than 8 and are co-prime with it.
So, phi(8) = 4

After we have phi_n, we can use that to get the private key:
d = gmpy2.invert(e, phi_n)  #where e is the public key

Now, with the pivate key and modulus n, we can decrypt the message
decrypted_message = pow(c, d, n)


"""

import sympy

# Prime Numbers
p = 69209246285341485176651677052094641923674678444770343539263565826655430979593
q = 74721145443370739851160612675283902507016607360836285751438617996337126152343

print(sympy.isprime(p))
print(sympy.isprime(q))

# Public Key
e = 65537

# Message
c = 1619361931505610889475080097598006023517541455892758232983551521804291139036613212938565838558870317082599445317816707390842265821757126896016520962374601

# Modulus n
n = p*q

# Euler's Totient Function of n
phi_n = (p-1) * (q-1)

# Inverting the public key with phi_n (we arn't using gmpy2 tho)
# Function to calculate modular multiplicative inverse
def mod_inv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1
d = mod_inv(e, phi_n)

decrypted_message = pow(c, d, n)
print(f"Private key (d): {d}")
print(f"Decrypted message: {bytearray.fromhex(hex(decrypted_message)[2:]).decode()}")



