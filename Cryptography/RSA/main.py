import sympy

# 1. Find Co-prime
def find_coprime(phi):
    e = 2
    flag = False
    while e < phi:
        if phi % e != 0:
            break
        else:
            e = e + 1
            flag = True
    if not flag:
        print("There is no co-prime with phi = " + str(phi))
        return -1000
    else:
        return e

# 2. Find 'd' having initial 'k'
def find_d(e, phi):
    d = 2
    while (d * e) % phi != 1:
        d = d + 1
    return d


# MAIN FUNCTION
# Public key (n, e)
# Private key (n, d)
LIM1 = 10**2
LIM2 = 10**3
x = sympy.randprime(LIM1, LIM2)
y = sympy.randprime(LIM1, LIM2)
while x == y:
    y = sympy.randprime(LIM1, LIM2)
n = x * y
phi = (x-1) * (y-1)
e = find_coprime(phi)
d = find_d(e, phi)
print("Public key  = (n, e) = (" + str(n) + ", " + str(e) + ")")
print("Private key = (n, d) = (" + str(n) + ", " + str(d) + ")")
message = 20
E = (message ** e) % n          # Encoded
D = (E ** d) % n                # Decoded
print()
print("message = " + str(message))
print("Encoded = " + str(E))
print("Decoded = " + str(D))
answer = input("Would you like to see the 2 random primes? ")
yes_list = ["yes", "yeah", "yep", "of course"]
if answer.lower() in yes_list:
    print("x = " + str(x) + ", y = " + str(y))