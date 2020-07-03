import numpy as np
import matplotlib.pyplot as plt

def visualize_line_code(line_code_name, x_axis, y_axis):
    plt.step(x_axis, y_axis)
    plt.title(line_code_name)
    plt.show()

def nrz_i():
    signal = 1
    y_axis = [signal]
    for bit in bit_sequence:
        if bit == 1:
            signal = -signal
            y_axis.append(signal)
        elif bit == 0:
            y_axis.append(signal)

    x_axis = np.arange(0, len(y_axis))
    
    visualize_line_code("NRZ-I", x_axis, y_axis)

def nrz_l():
    signal = 1
    y_axis = [signal]
    for bit in bit_sequence:
        if bit == 1:
            signal = -1
            y_axis.append(signal)
        elif bit == 0:
            signal = 1
            y_axis.append(signal)

    x_axis = np.arange(0, len(y_axis))

    visualize_line_code("NRZ-L", x_axis, y_axis)

def pseudoternary():
    pass
def manchester():
    pass
def differential_manchester():
    pass

if __name__ == "__main__":    
    while True:
        print("\nEnter the bit sequence separating the bits with a space:")
        bit_sequence = [int(i) for i in input().split()]

        option = int(input("0 - Quit \n1 - NRZ-I \n2 - NRZ-L \n3 - Pseudoternary\n4 - Manchester\n5 - Differential Manchester\n"))

        if option == 0:
            quit()
        elif option == 1:
            nrz_i()
        elif option == 2:
            nrz_l()
        elif option == 3:
            pseudoternary()
        elif option == 4:
            manchester()
        elif option == 5:
            differential_manchester()
        else:
            print("Choose a valid option!\n")