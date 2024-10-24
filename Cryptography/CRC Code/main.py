from random import randrange

# Function 1 - Calculate XOR
def XOR(number1, number2):
    if len(number1) != len(number2):
        print("Error while calculating function '" + XOR.__name__ + "'")
        return -1000
    # print("XOR between", number1, number2)
    N = len(number1)
    result = ""
    for i in range(N):
        if number1[i] == number2[i]:
            result += "0"
        else:
            result += "1"
    return result


# Function 2 - Simulate
def simulate():
    # 1. Create a bitstream named "D"
    limit1 = 10
    limit2 = 20
    length = randrange(limit1, limit2+1)
    D = [str(randrange(2)) for i in range(length)]
    D = "".join(D)
    d = len(D)

    # 2. Create a random number
    limit1 = 0.3 * limit1
    limit2 = 0.3 * limit2
    length = randrange(int(limit1), int(limit2)+1)
    R_initial = [str(0) for i in range(length)]
    R_initial = "".join(R_initial)
    r = len(R_initial)
    DR_initial = D + R_initial
    # print(D, R_initial, DR_initial)

    # 3. Create a generator function G. It must begin with 1
    g = r + 1
    G = [str(randrange(2)) for i in range(g)]
    G[0] = "1"
    G = "".join(G)
    # print()
    # print(G, "    ", DR_initial)

    # 4. Ready to divide with XOR logic
    # First, I will produce G' = G * 0 (same digits number)
    GG = ["0" for i in range(g)]
    GG = "".join(GG)
    times = len(DR_initial) + 1 - g
    result = ""
    # Initialization
    segment = DR_initial[0:g]
    segment = "".join(segment)
    if segment[0] == "1":
        result = XOR(segment, G)
        # print("Seg = " + segment + ", G = " + G + ", result = " + result)
    else:
        result = XOR(segment, GG)
        # print("Seg = " + segment + ", GG = " + GG + ", result = " + result)

    for i in range(times-1):
        # Now, result has length = g, but the first digit IS ALWAYS 0
        # So, I will remove the first zero and then I will add in the letter's word the next digit of D * 2^r
        segment = result[1:]
        segment += DR_initial[i+g]
        segment = "".join(segment)
        if segment[0] == "1":
            result = XOR(segment, G)
            # print("Seg = " + segment + ", G = " + G + ", result = " + result)
        else:
            result = XOR(segment, GG)
            # print("Seg = " + segment + ", GG = " + GG + ", result = " + result)

    # After all this procedure, we have ended with a g-length word "result"
    # The 1st bit of the word is for sure "0", because of our XOR logic
    # r = g-1 = the number of EDC bits ----> so, I have to remove the 1st bit = 0 from "result"
    result = result[1:]
    print("*******************************************************************************")
    print("D = " + D + "    G = " + G + "       (d = " + str(d) + ", g = " + str(g) + ", r = " + str(r) + ")")
    print("D * 2^r = " + DR_initial)
    print()
    print(G + "    |     " + DR_initial)
    print("--------------------------------")
    R = result
    DR_final = D + R
    print("R = " + R)
    print()
    print("<D,R> = " + DR_final)
    print("*******************************************************************************")


# MAIN FUNCTION
simulate()