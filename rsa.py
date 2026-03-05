import random

# ===============================
# 1. Utility Functions
# ===============================

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd_val, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd_val, x, y

def mod_inverse(e, phi):
    gcd_val, x, y = extended_gcd(e, phi)
    if gcd_val != 1:
        return None
    return x % phi

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime(start=50, end=200):
    while True:
        num = random.randint(start, end)
        if is_prime(num):
            return num

def power(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result

# ===============================
# 2. Key Generation
# ===============================

print("\n=== RSA KEY GENERATION ===")

p = generate_prime()
q = generate_prime()

while q == p:
    q = generate_prime()

print("Prime p:", p)
print("Prime q:", q)

n = p * q
phi = (p - 1) * (q - 1)

print("n (p*q):", n)
print("phi(n):", phi)

e = random.randint(2, phi - 1)
while gcd(e, phi) != 1:
    e = random.randint(2, phi - 1)

d = mod_inverse(e, phi)

print("Public Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))

# ===============================
# 3. Encryption
# ===============================

print("\n=== ENCRYPTION ===")

message = input("Masukkan plaintext: ")

# Convert string ke ASCII
plaintext_numbers = [ord(char) for char in message]
print("ASCII:", plaintext_numbers)

ciphertext = [power(num, e, n) for num in plaintext_numbers]
print("Ciphertext:", ciphertext)

# ===============================
# 4. Decryption
# ===============================

print("\n=== DECRYPTION ===")

decrypted_numbers = [power(num, d, n) for num in ciphertext]
print("Decrypted ASCII:", decrypted_numbers)

decrypted_message = ''.join([chr(num) for num in decrypted_numbers])
print("Recovered Plaintext:", decrypted_message)