# RSA From Scratch – Terminal Edition

Implementasi algoritma RSA (Rivest–Shamir–Adleman) dari awal (from scratch) menggunakan Python tanpa library kriptografi instan.

Program ini dibuat untuk memenuhi tugas Analisis Komprehensif Kriptografi dalam Konteks Confidentiality.

Author: Thoriq

---

## Deskripsi

Program ini mendemonstrasikan:

- Pembangkitan kunci RSA (Key Generation)
- Proses Enkripsi (Plaintext → Ciphertext)
- Proses Dekripsi (Ciphertext → Plaintext)
- Implementasi Extended Euclidean Algorithm
- Modular Exponentiation
- Konversi String ke ASCII dan sebaliknya

Tampilan dibuat dalam gaya terminal cybersecurity untuk mendukung visualisasi konsep.

---

## Konsep RSA yang Diimplementasikan

1. Memilih dua bilangan prima (p dan q)
2. Menghitung:
   - n = p × q
   - φ(n) = (p−1)(q−1)
3. Memilih e sehingga gcd(e, φ(n)) = 1
4. Menghitung d sebagai modular inverse dari e terhadap φ(n)
5. Enkripsi:
   C = M^e mod n
6. Dekripsi:
   M = C^d mod n

---

## Cara Menjalankan Program

### 1. Pastikan Python Terinstall

Cek dengan:

```bash
python --version
```
run program:

```bash
python3 tugasrsa.py
```
