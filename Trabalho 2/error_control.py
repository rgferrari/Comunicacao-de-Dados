"""
Members: René Gargano Ferrari, Artur Sendtko, Augusto Gai Dal'Asta, 
         Leonarno Aita de Oliveira Militz.
"""

def is_bit_sequence_valid(bit_seq):
    for bit in bit_seq:
        if bit != '0' and bit != '1':
            return False
    
    return True

def fix_bit_sequence(bit_seq):
    modulo = len(bit_seq) % 16

    while modulo != 0:
        bit_seq = '0' + bit_seq
        modulo = len(bit_seq) % 16
    
    return bit_seq
        

def separate_bit_sequence(bit_seq):
    n_arrays = int(len(bit_seq) / 16)

    bit_sequence_list = []
    iterator = 16
    for i in range(n_arrays):
        begin = iterator - 16
        bit_sequence_list.append(bit_seq[begin:iterator])
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

def ones_complement(bit_string):
    complement = ''
    for bit in bit_string:
        if bit == '0':
            complement += '1'
        if bit == '1':
            complement += '0'
    
    return complement

def reverse_eng_info(bit_string_list):

    size_check = []
    total_size  = 0

    for sequence in bit_string_list:
        size_check.append(len(sequence))
        total_size += len(sequence)

    print("\nSequences sizes: " + str(size_check))
    print("Total size: " + str(total_size))


def checksum16(bit_sequence):
    bit_sequence = fix_bit_sequence(bit_sequence)
    bit_sequence_list = separate_bit_sequence(bit_sequence)
    
    summatory = bit_sequence_list[0]

    if len(bit_sequence_list) >= 2:
        for i in range(1, len(bit_sequence_list)):

            summatory = add_binary_nums(summatory, bit_sequence_list[i])

            if len(summatory) > 16:
                last_bit = summatory[0]
                summatory = summatory[1:]
                summatory = add_binary_nums(summatory, last_bit)

    summatory = ones_complement(summatory)
    bit_sequence_list.append(summatory)
    reverse_eng_info(bit_sequence_list)

    return bit_sequence_list


def input_type_menu():
    while True:
        input_option = int(input(
"""
Select an input option:

0. String (ex: "Hello World")
1. Binary Sequence (ex: "101010110111001")

"""
            ))
        
        if   input_option == 0: string_input_menu()
        elif input_option == 1: binary_input_menu()
        else: print("\nChoose a valid option!") 

def binary_input_menu():
    want_new_bit_sequence = True
    
    while True:
        if want_new_bit_sequence: 
            bit_sequence = input("\nEnter the bit sequence to operate. \n>> ")
            
            if (is_bit_sequence_valid(bit_sequence)):
                want_new_bit_sequence = False
            else:
                print("\nnot a bit sequence.")
                want_new_bit_sequence = True

        if want_new_bit_sequence == False:
            option = int(input("\nChoose an option: \n0 - Quit \n1 - Enter a new input \n2 - Checksum 16\n"))

            if   option == 0: quit()
            elif option == 1: return
            elif option == 2:
                print("\n", checksum16(bit_sequence), sep="")
                input("\nPress 'Enter' to continue...")
            else: print("\nChoose a valid option!")

def string_input_menu():
    want_new_bit_sequence = True
    
    while True:  
        if want_new_bit_sequence: 
            user_input = input("\nEnter the string to operate. \n>> ")
            bit_sequence = ''.join(format(ord(x), 'b') for x in user_input)
            print("\nYour string in binary values:\n" + bit_sequence + "\nBinary String Size: " + str(len(bit_sequence)))
            
            want_new_bit_sequence = False

        if want_new_bit_sequence == False:
            option = int(input("\nChoose an option: \n0 - Quit \n1 - Enter a new input \n2 - Checksum 16\n"))

            if   option == 0: quit()
            elif option == 1: return
            elif option == 2:
                print("\n", checksum16(bit_sequence), sep="")
                input("\nPress 'Enter' to continue...")
            else: print("\nChoose a valid option!")

if __name__ == "__main__":
    input_type_menu()
