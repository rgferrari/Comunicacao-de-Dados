import numpy as np
import matplotlib.pyplot as plt

def visualize_line_code(line_code_name, x_axis, y_axis):
    plt.step(x_axis, y_axis)
    plt.title(line_code_name)
    plt.show()

# Fiz so pra testar o matplotlib
def nrz():
    x_axis = np.arange(0, len(bit_sequence))
    y_axis = bit_sequence
    plt.step(x_axis, y_axis)
    plt.title("NRZ-I")
    plt.show()

def nrz_i():
    signal = 1
    x_axis = np.arange(0, len(bit_sequence) + 1)
    y_axis = [signal]
    for bit in bit_sequence:
        if bit == 1:
            signal = -signal
            y_axis.append(signal)
        if bit == 0:
            y_axis.append(signal)
    
    visualize_line_code("NRZ-I", x_axis, y_axis)

def nrz_l():
    pass
def pseudoternary():
    pass
def manchester():
    pass
def differential_manchester():
    pass

if __name__ == "__main__":    
    while True:
        print("Enter the bit sequence separating the bits with a space:")
        bit_sequence = [int(i) for i in input().split()]

        option = int(input("0 - Quit \n1 - NRZ-I \n2 - NRZ-L \n3 - Pseudoternary\n4 - Manchester\n5 - Differential Manchester\n"))
        if option == 0:
            quit()
        elif option == 1:
            nrz_i()
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            pass
        else:
            print("Choose a valid option!\n")