"""
Members: René Gargano Ferrari, Artur Sendtko, Augusto Gai Dal'Asta, Leonarno Aita Militz.
Insert the bit sequence with a space between the bits as in the example as follows:
0 1 0 1 1 1 0 1 0 1
"""
import numpy as np

def bitSequenceValid():
    for bit in bit_sequence:
        if bit != 0 and bit != 1:
            return False
    
    return True

def fix_bit_sequence():
    modulo = len(bit_sequence) % 16

    while modulo != 0:
        bit_sequence.insert(0, 0)
        modulo = len(bit_sequence) % 16
        

def separate_bit_sequence():
    n_arrays = int(len(bit_sequence) / 16)

    bit_sequence_list = []
    iterator = 16
    for i in range(n_arrays):
        begin = iterator - 16
        bit_sequence_list.append(bit_sequence[begin:iterator])
        iterator += 16
    
    return bit_sequence_list

def add_binary_nums(x, y): 
    max_len = max(len(x), len(y)) 

    x = x.zfill(max_len) 
    y = y.zfill(max_len) 
        
    # initialize the result 
    result = '' 
        
    # initialize the carry 
    carry = 0

    # Traverse the string 
    for i in range(max_len - 1, -1, -1): 
        r = carry 
        r += 1 if x[i] == '1' else 0
        r += 1 if y[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result 
        carry = 0 if r < 2 else 1     # Compute the carry. 
        
    if carry !=0 : result = '1' + result 

    return result.zfill(max_len) 

def bit_to_string(bit_seq):
    string = ''
    for bit in bit_seq:
        string = string + (str(bit))
    
    return string

def ones_complement(bit_string):
    complement = ''
    for bit in bit_string:
        if bit == '0':
            complement += '1'
        if bit == '1':
            complement += '0'
    
    return complement


def checksum16():
    fix_bit_sequence()
    bit_sequence_list = separate_bit_sequence()
        
    binary_string_list = []
    for sequence in bit_sequence_list:
        binary_string_list.append(bit_to_string(sequence))

    
    summatory = binary_string_list[0]

    if len(binary_string_list) >= 2:
        for i in range(1, len(binary_string_list)):

            summatory = add_binary_nums(summatory, binary_string_list[i])

            if len(summatory) > 16:
                last_bit = summatory[0]
                summatory = summatory[1:]
                summatory = add_binary_nums(summatory, last_bit)

    summatory = ones_complement(summatory)

    binary_string_list.append(summatory)

    return binary_string_list


if __name__ == "__main__":
    want_new_bit_sequence = True    
    
    while True:  
        if want_new_bit_sequence:
            print("\nEnter the bit sequence separating the bits with a space:")
            bit_sequence = [int(i) for i in input().split()]
            
            if (bitSequenceValid()):
                want_new_bit_sequence = False
            else:
                print("\nnot a bit sequence.")
                want_new_bit_sequence = True

        if want_new_bit_sequence == False:
            option = int(input("\nChoose an option: \n0 - Quit \n1 - Enter a new bit sequence \n2 - Checksum 16\n"))

            if   option == 0: quit()
            elif option == 1: want_new_bit_sequence = True
            elif option == 2:
                print("\n", checksum16(), sep="")
                input("\nPress 'Enter' to continue...")
            else: print("\nChoose a valid option!")