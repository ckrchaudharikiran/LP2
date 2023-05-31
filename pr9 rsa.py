from math import gcd
msg = int(input("Enter the number to be encrypted and decrypted: "))
p, q = map(int, input("Enter 1st prime number p and 2nd prime number q: ").split())
n = p * q
z = (p - 1) * (q - 1)
e = next(i for i in range(2, z) if gcd(i, z) == 1)
def find_mod_inverse(e, z):
    for d in range(1, z):
        if (e * d) % z == 1:
            return d
d = find_mod_inverse(e, z)
c = pow(msg, e, n)
msgback = pow(c, d, n)
print("Encrypted message is:", c)
print("Decrypted message is:", msgback)
print("The value of z =", z)
print("The value of e =", e)
print("The value of d =", d)
