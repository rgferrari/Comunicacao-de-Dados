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

def twoDimParity():
    pass

def checksum16():
    pass

def crc16():
    pass

def hamming():
    pass

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
                2 - Two-dimensional parity-check
                3 - Checksum 16-bits
                4 - CRC-16: x^16 + x^12 + x^5 + 1
                5 - Hamming
                """
            ))

            if   option == 0: quit()
            elif option == 1: want_new_bit_sequence = True
            elif option == 2: twoDimParity()
            elif option == 3: checksum16()
            elif option == 4: crc16()
            elif option == 5: hamming()
            else: print("\nChoose a valid option!")