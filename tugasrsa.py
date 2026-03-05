import random
import time
import os

# ===============================
# COLOR (ANSI ESCAPE CODE)
# ===============================
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# ===============================
# CLEAR SCREEN
# ===============================
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ===============================
# HACKER ASCII ART
# ===============================
def hacker_banner():
    print(GREEN + r"""
     ██████╗ ███████╗ █████╗ 
     ██╔══██╗██╔════╝██╔══██╗
     ██████╔╝███████╗███████║
     ██╔══██╗╚════██║██╔══██║
     ██║  ██║███████║██║  ██║
     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

        >>> SECURE TERMINAL <<<
        RSA ENCRYPTION SYSTEM
            by Thoriq
    """ + RESET)

# ===============================
# LOADING EFFECT
# ===============================
def loading(text):
    print(CYAN + text, end="", flush=True)
    for _ in range(5):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print(RESET)

# ===============================
# RSA FUNCTIONS
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

def generate_prime(start=100, end=300):
    while True:
        num = random.randint(start, end)
        if is_prime(num):
            return num

def power(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result

# ===============================
# MAIN PROGRAM
# ===============================

clear()
hacker_banner()
loading("Initializing secure RSA engine")

print(YELLOW + "\n[+] Generating prime numbers..." + RESET)
p = generate_prime()
q = generate_prime()

while q == p:
    q = generate_prime()

time.sleep(1)
print(GREEN + f"[✓] Prime p = {p}")
print(f"[✓] Prime q = {q}" + RESET)

n = p * q
phi = (p - 1) * (q - 1)

print(YELLOW + "\n[+] Computing keys..." + RESET)

e = random.randint(2, phi - 1)
while gcd(e, phi) != 1:
    e = random.randint(2, phi - 1)

d = mod_inverse(e, phi)

time.sleep(1)
print(GREEN + f"[✓] Public Key (e,n) = ({e}, {n})")
print(f"[✓] Private Key (d,n) = ({d}, {n})" + RESET)

# ===============================
# ENCRYPTION
# ===============================

print(CYAN + "\n=== ENCRYPTION MODE ===" + RESET)
message = input(GREEN + "Enter message: " + RESET)

plaintext_numbers = [ord(char) for char in message]
ciphertext = [power(num, e, n) for num in plaintext_numbers]

loading("Encrypting message")
print(RED + f"\n[Encrypted Data] → {ciphertext}" + RESET)

# ===============================
# DECRYPTION
# ===============================

print(CYAN + "\n=== DECRYPTION MODE ===" + RESET)
loading("Decrypting message")

decrypted_numbers = [power(num, d, n) for num in ciphertext]
decrypted_message = ''.join(chr(num) for num in decrypted_numbers)

print(GREEN + f"\n[Recovered Message] → {decrypted_message}" + RESET)

print(YELLOW + "\nSystem Secure. Transmission Completed." + RESET)