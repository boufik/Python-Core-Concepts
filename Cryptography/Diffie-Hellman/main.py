# Publicly known (2 public)
p = 23
g = 5                # g = 5 is a primitive root modulo 23
# PRIVATE (2 private)
a = 6
b = 15
# Publicly known (4 public)
A = g**a % p
B = g**b % p
# Receiving
sA = B**a % p
sB = A**b % p
# PRIVATE: the same shared key (3 private)
s = sA if sA == sB else None
print(f"Shared key = {s}")
