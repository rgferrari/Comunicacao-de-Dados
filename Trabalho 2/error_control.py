"""
Members: René Gargano Ferrari, Artur Sendtko, Augusto Gai Dal'Asta, Leonarno Aita Militz.
Insert the bit sequence with a space between the bits as in the example as follows:
0 1 0 1 1 1 0 1 0 1
"""
import numpy as np
import math

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


def checksum16():
    fix_bit_sequence()
    bit_sequence_list = separate_bit_sequence()

    stringList = ''.join([str(item) for item in bit_sequence_list[0]])

    binaryList = ''.join(format(ord(item), 'b') for item in stringList)

    print(binaryList)


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
            option = int(input(
                """
Choose an option: 
0 - Quit 
1 - Enter a new bit sequence 
2 - Checksum 16
"""
            ))

            if   option == 0: quit()
            elif option == 1: want_new_bit_sequence = True
            elif option == 2: checksum16()
            else: print("\nChoose a valid option!")