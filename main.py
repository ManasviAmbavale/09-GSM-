import random

# Generate 128-bit key and message
k = random.getrandbits(128)
m = random.getrandbits(128)

# Convert to binary
kb = bin(k)[2:]
mb = bin(m)[2:]

# Split into halves
kbl = kb[0:64]
kbr = kb[64:]
mbl = mb[0:64]
mbr = mb[64:]

# XOR operations
a1 = int(kbl, 2) ^ int(mbr, 2)
a2 = int(kbr, 2) ^ int(mbl, 2)
a3 = a1 ^ a2

# Convert back to binary
a4 = bin(a3)[2:].zfill(64)

# Split and recombine
a5 = a4[0:32]
a6 = a4[32:]
a7 = int(a5, 2) ^ int(a6, 2)

# Output
print("128 Bit Key =", kb)
print("128 Random Bits Generated =", mb)
print("RES/SRES =", bin(a7)[2:].zfill(len(a5)))
