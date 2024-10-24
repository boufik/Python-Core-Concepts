from math import log2
from random import randrange
import copy

# Function 1 ---> 2^r >= m + r + 1
def find_r(m):
    r = 0
    while 2**r - r < m + 1:
        r = r + 1
    return r

# Function 2 - Decimal to binary
def dec_to_bin(decimal):
    # decimal = INTEGER
    if decimal == 0:
        return [0]
    else:
        digits = list()
        LEN = int(log2(decimal)) + 1
        for exp in range(LEN-1, -1, -1):
            value = 2 ** exp
            if decimal >= value:
                digits.append(1)
                decimal -= value
            else:
                digits.append(0)
        return digits


# Function 3 - Binary to decimal
def bin_to_dec(binary):
    # binary = LIST
    SUM = 0
    LEN = len(binary)
    for index in range(LEN):
        SUM += binary[index] * (2**(LEN-1-index))
    return SUM


# Function 4 - Padding with zeros
def pad_zeros(binary, LEN):
    LEN1 = int(log2(LEN)) + 1
    LEN2 = len(binary)
    binary2 = [0 for i in range(LEN1 - LEN2)]
    binary = binary2 + binary
    return binary


# Function 5 - Binary representation of indeces
def bin_representation(LEN):
    # If LEN = 11, I will create a list with all the binary representations of numbers
    # between 11 and 1 (inclusively)
    indeces_binary = list()
    for i in range(LEN, 0, -1):
        binary = dec_to_bin(i)
        indeces_binary.append(pad_zeros(binary, LEN))
    return indeces_binary



# Function 6 - Write the codeword without redundant bits
def write_codeword_no_redundant(data, m, r, LEN):
    # I will symbolize redundant with the number '-1'
    codeword_no_redundant = list()
    counter = 0
    for i in range(LEN, 0, -1):
        if log2(i) == int(log2(i)):
            codeword_no_redundant.append(-1)
        else:
            codeword_no_redundant.append(data[counter])
            counter += 1
    return codeword_no_redundant



# Function 7 - Parity bits
def determine_parity(codeword_no_redundant, m, r, LEN, indeces_binary):
    # There will be 'r' parity bits in the word
    # print()
    par_bits = list()
    par_bits_check_pos = list()
    for par_exp in range(r):
        # print("par_exp = ", par_exp)
        # r = 4, par_exp = (0, 1, 2, 3)
        # Assuming r = 2, check the 2nd position (index 1) from binary representation of indeces
        pos_check = r - 1 - par_exp
        # I will check how many 1's are there in positions with index pos_check
        SUM = 0
        par_exp_check_pos = list()
        for i in range(len(indeces_binary)):
            index_binary = indeces_binary[i]
            if index_binary[pos_check] == 1:
                par_exp_check_pos.append(bin_to_dec(index_binary))
                # print(bin_to_dec(index_binary))
                value = codeword_no_redundant[i]
                # print("Value = ", value)
                if value != -1:
                    SUM += value
        # SUM IS OK by now
        # print("SUM = ", SUM)
        par_bits_check_pos.append(par_exp_check_pos)
        par_bit = SUM % 2
        par_bits.append(par_bit)
        # print()
    # Now, I have to flip my list with parity bits
    par_bits.reverse()
    par_bits_check_pos.reverse()
    return par_bits, par_bits_check_pos



# Function 8 - Fill with parity bits
def fill_with_parity(codeword_no_redundant, par_bits):
    codeword = copy.deepcopy(codeword_no_redundant)
    counter = 0
    for i in range(len(codeword)):
        if codeword[i] == -1:
            codeword[i] = par_bits[counter]
            counter += 1
    return codeword, codeword_no_redundant




# Function 9 - Hamming coded data message
def Hamming_in_data(data):
    # 1. Initialization of parameters
    r = find_r(m)
    LEN = m + r         # Codeword length
    # 2. Codeword without redundant
    codeword_no_redundant = write_codeword_no_redundant(data, m, r, LEN)
    # 3. Determine the missing positions of a codeword = message + redundant
    indeces_binary = bin_representation(LEN)
    par_bits, par_bits_check_pos = determine_parity(codeword_no_redundant, m, r, LEN, indeces_binary)
    # 4. Fill the gaps (-1) in codeword with this list
    codeword, codeword_no_redundant = fill_with_parity(codeword_no_redundant, par_bits)
    return codeword_no_redundant, par_bits, par_bits_check_pos, codeword



# Function 10 - Error detection and correction
def error_correction(codeword, indeces, LEN):
    digits = list()
    for i in range(len(indeces)):
        index = indeces[i]
        SUM = 0
        for j in range(len(index)):
            index_check = LEN - index[j]
            SUM += codeword[index_check]
        digits.append(SUM % 2)
    return digits



# Function 11 - Simulate Hamming Error Correction
def Hamming_correct(data, codeword_no_redundant, par_bits, par_bits_check_pos, codeword):
    LEN = len(codeword)
    print()
    print(120 * "*")
    print(" Lengths =  " + str(len(data)) + ", " + str(len(par_bits)) + ", " + str(len(codeword)))
    print("    Data =  " + str(data))
    # print("No_redun =  " + str(codeword_no_redundant))
    print("Par_bits =  " + str(par_bits))
    print("Codeword =  " +  str(codeword))
    # Suppose in receiver there is a single error in a single index of the codeword sent
    # So, in 'index_error', the '0' becomes '1' and the '1' becomes '0'
    # 0 ---> 1 or 1 ---> 0 by this way: rec = 1 - tr
    index_error = randrange(LEN)
    codeword[index_error] = 1 - codeword[index_error]
    # print()
    print("------> Error in position " + str(LEN - index_error) + " from the right (index " + str(index_error) + ") <------")
    print("Received = ", codeword)
    # print("Indeces to be checked = " + str(par_bits_check_pos))
    # Now, I have the received message containing a single error. I follow the appropriate process for error detection
    digits = error_correction(codeword, par_bits_check_pos, LEN)
    digits_str = [str(element) for element in digits]
    print("------> Error occured in position " + ''.join(digits_str) + " = " + str(bin_to_dec(digits)) + " <------")
    print(120 * "*")



# MAIN FUNCTI0N
low = 10
high = 20
m = randrange(low, high + 1)
data = [randrange(2) for i in range(m)]
codeword_no_redundant, par_bits, par_bits_check_pos, codeword = Hamming_in_data(data)
Hamming_correct(data, codeword_no_redundant, par_bits, par_bits_check_pos, codeword)

