import numpy as np
import matplotlib.pyplot as plt

def visualize_line_code(line_code_name, x_axis, y_axis):
    # Set the marked values at axis x and y
    plt.yticks([-1, 0, 1])
    plt.xticks(x_axis)

    # Create the time line in the middle
    time_line = [0] * len(x_axis)
    plt.plot(x_axis, time_line, color="black", linewidth="0.5")

    # Create the vertical dashed lines for each bit
    for i in x_axis:
        dashed_line = [i] * len(y_axis)
        plt.plot(dashed_line, y_axis, dashes=[10, 15], color="black", linewidth="0.5")

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

    visualize_line_code("Pseudoternary", x_axis, y_axis)

def manchester():
    y_axis = [1]

    for bit in bit_sequence:
        if bit == 1:
            y_axis.append(-1)
            y_axis.append(1)

        if bit == 0:
            y_axis.append(1)
            y_axis.append(-1)

            
    x_axis = np.arange(0, len(y_axis))

    visualize_line_code("Manchester", x_axis, y_axis)
    
def differential_manchester():
    signal = 1
    y_axis = [signal]

    for bit in bit_sequence:
        if bit == 1:
            y_axis.append(signal)
            y_axis.append(-signal)

            signal = -signal

        if bit == 0:
            signal = -signal

            y_axis.append(signal)
            y_axis.append(-signal)

            signal = -signal
            
    x_axis = np.arange(0, len(y_axis))

    visualize_line_code("Differential Manchester", x_axis, y_axis)

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
            nrz_l()
        elif option == 3:
            pseudoternary()
        elif option == 4:
            manchester()
        elif option == 5:
            differential_manchester()
        else:
            print("Choose a valid option!\n")