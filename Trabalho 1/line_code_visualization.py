"""
Members: René Gargano Ferrari, Artur Sendtko, Augusto Gai Dal'Asta, Leonarno Aita Militz.
Insert the bit sequence with a space between the bits as in the example as follows:
0 1 0 1 1 1 0 1 0 1
"""

import numpy as np
import matplotlib.pyplot as plt

def visualize_line_code(line_code_name, x_axis, y_axis, yticks):
    # Set the marked values at axis x and y
    plt.yticks(yticks)
    # Show only the integer values in x_axis
    xticks_x_axis = x_axis[x_axis == x_axis.astype(int)] 
    plt.xticks(xticks_x_axis)

    # Create the vertical dashed lines for each bit
    plt.grid(axis="x", color="black", linestyle="--", linewidth="0.5", dashes=(6,6))

    plt.step(x_axis, y_axis, color="red")
    plt.title(line_code_name)
    plt.xlabel("Time")
    plt.ylabel("Level")
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

    # Create the time line in the middle
    plt.axhline(0, linestyle="-", color="black", linewidth="0.5")
    
    visualize_line_code("NRZ-I", x_axis, y_axis, [-1, 0, 1])

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

    # Create the time line in the middle
    plt.axhline(0, linestyle="-", color="black", linewidth="0.5")

    visualize_line_code("NRZ-L", x_axis, y_axis, [-1, 0, 1])

def pseudoternary():
    signal = 1
    positivo = True
    y_axis = [signal]
    for bit in bit_sequence:
        if bit == 1:
            signal = 0
            y_axis.append(signal)
        elif bit == 0:
            if positivo:
                signal = 1
                positivo = False
            else:
                signal = -1
                positivo = True
            y_axis.append(signal)

    x_axis = np.arange(0, len(y_axis))

    # Create the time line in the middle
    plt.axhline(0, linestyle="-", color="black", linewidth="0.5")

    visualize_line_code("Pseudoternary", x_axis, y_axis, [-1, 0, 1])

def manchester():
    y_axis = [1]

    for bit in bit_sequence:
        if bit == 1:
            y_axis.append(0)
            y_axis.append(1)

        if bit == 0:
            y_axis.append(1)
            y_axis.append(0)

            
    x_axis = np.arange(start=0, stop=len(y_axis)/2, step=0.5)

    # Create the time line in the middle
    plt.axhline(0.5, linestyle="-", color="black", linewidth="0.5")

    visualize_line_code("Manchester", x_axis, y_axis, [0, 1])
    
def differential_manchester():
    signal = 1
    y_axis = [signal]

    for bit in bit_sequence:
        if bit == 1:
            y_axis.append(signal)
            y_axis.append(1 - signal)

            signal = 1 - signal

        if bit == 0:
            signal = 1 - signal

            y_axis.append(signal)
            y_axis.append(1 - signal)

            signal = 1 - signal
            
    x_axis = np.arange(start=0, stop=len(y_axis)/2, step=0.5)

    # Create the time line in the middle
    plt.axhline(0.5, linestyle="-", color="black", linewidth="0.5")    

    visualize_line_code("Differential Manchester", x_axis, y_axis, [0, 1])

if __name__ == "__main__":
    want_new_bit_sequence = True    
    while True:
        if want_new_bit_sequence:
            print("\nEnter the bit sequence separating the bits with a space:")
            bit_sequence = [int(i) for i in input().split()]
            want_new_bit_sequence = False

        option = int(input("\nChoose an option: \n0 - Quit \n1 - Enter a new bit sequence \n2 - NRZ-I \n3 - NRZ-L \n4 - Pseudoternary\n5 - Manchester\n6 - Differential Manchester\n"))

        if option == 0:
            quit()
        elif option == 1:
            want_new_bit_sequence = True
        elif option == 2:
            print("\nShowing visualization...")
            nrz_i()
        elif option == 3:
            print("\nShowing visualization...")
            nrz_l()
        elif option == 4:
            print("\nShowing visualization...")
            pseudoternary()
        elif option == 5:
            print("\nShowing visualization...")
            manchester()
        elif option == 6:
            print("\nShowing visualization...")
            differential_manchester()
        else:
            print("\nChoose a valid option!")