from tkinter import *                                                               # Tkinter (GUI) imported
import random                                                                       # random to choose word


class Application(Frame):                                                           # Define a class to extend Frame
    globalnumber = 1


def calc_mean():                                                                    # Function to calculate mean
    try:
        num_list = (numlist.get()).split(',')                                       # Split numbers from number list
        i = 0                                                                       # Initialize i for loop
        while i < len(num_list) - 1:
            if float(num_list[i]) < 0:                                              # Prevent number less than 0
                Label(root, text="Please enter numbers greater than 0.").grid()     # Tell user to input a number greater than 0
                flag = 0                                                            # Change flag to 0
                break                                                               # Break the loop
            else:
                flag = 1                                                            # Change flag to 1
            i += 1                                                                  # Increase i
        if flag == 1:                                                               # When flag = 1
            num_list = sorted(list(map(float, num_list)))                           # Create a sorted list from input
            total_num = sum(num_list)                                               # Sum of numbers
            mean = total_num / len(num_list)                                        # Calculate mean
            Label(root, text="Mean is: " + str(mean)).grid()                        # Show the result
            Label(root, text="Did you get the same answer?").grid()                 # Tell user to select if they do it correctly
            Button(root, text="Yes", command=yes).grid()                            # Display a "Yes" button
            Button(root, text="No", command=no).grid()                              # Display a "No" button
    except:                                                                         # Exception when value gets error
        Label(root, text="Please Enter Appropriate Values.").grid()



def calc_median():                                                                  # Function to calculate mean
    try:
        num_list = (numlist.get()).split(',')                                       # Split numbers from number list
        i = 0                                                                       # Initialize i for loop
        while i < len(num_list) - 1:
            if float(num_list[i]) < 0:                                              # Prevent number less than 0
                Label(root, text="Please enter numbers greater than 0.").grid()     # Tell user to input a number greater than 0
                flag = 0                                                            # Change flag to 0
                break                                                               # Break the loop
            else:
                flag = 1                                                            # Change flag to 1
            i += 1                                                                  # Increase i
        if flag == 1:                                                               # When flag = 1
            num_list = sorted(list(map(float, num_list)))                           # Create a sorted list from input
            half = len(num_list) // 2                                               # Define "half" as middle number in list
            median = (num_list[half] + num_list[~half]) / 2                         # Calculate median
            Label(root, text="Median is: " + str(median)).grid()                    # Show the result
            Label(root, text="Did you get the same answer?").grid()                 # Tell user to select if they do it correctly
            Button(root, text="Yes", command=yes).grid()                            # Display a "Yes" button
            Button(root, text="No", command=no).grid()                              # Display a "No" button
    except:                                                                         # Exception when value gets error
        Label(root, text="Please Enter Appropriate Values.").grid()


def calc_mode():                                                                    # Function to calculate mode
    try:
        num_list = (numlist.get()).split(',')                                       # Split numbers from number list
        i = 0                                                                       # Initialize i for loop
        while i < len(num_list) - 1:
            if float(num_list[i]) < 0:                                              # Prevent number less than 0
                Label(root, text="Please enter numbers greater than 0.").grid()     # Tell user to input a number greater than 0
                flag = 0                                                            # Change flag to 0
                break                                                               # Break the loop
            else:
                flag = 1                                                            # Change flag to 1
            i += 1                                                                  # Increase i
        if flag == 1:                                                               # When flag = 1
            num_list = sorted(list(map(float, num_list)))                             # Create a sorted list from input
            mode = []                                                               # Create a mode list
            num_dict = dict((a, num_list.count(a)) for a in num_list)               # Create a dict from num_list
            if max(num_dict.values()) == 1:                                         # Process to solve result
                pass
            else:
                for k, v in num_dict.items():
                    if v == max(num_dict.values()):
                        mode.append(k)
            Label(root, text="Mode is: " + str(mode)).grid()                        # Show the result
            Label(root, text="Did you get the same answer?").grid()                 # Tell user to select if they do it correctly
            Button(root, text="Yes", command=yes).grid()                            # Display a "Yes" button
            Button(root, text="No", command=no).grid()                              # Display a "No" button
    except:                                                                         # Exception when value gets error
        Label(root, text="Please Enter Appropriate Values.").grid()


def calc_std():                                                                     # Function to calculate stdev
    try:
        num_list = (numlist.get()).split(',')                                       # Split numbers from number list
        i = 0                                                                       # Initialize i for loop
        while i < len(num_list) - 1:
            if float(num_list[i]) < 0:                                              # Prevent number less than 0
                Label(root, text="Please enter numbers greater than 0.").grid()     # Tell user to input a number greater than 0
                flag = 0                                                            # Change flag to 0
                break                                                               # Break the loop
            else:
                flag = 1                                                            # Change flag to 1
            i += 1                                                                  # Increase i
        if flag == 1:                                                               # When flag = 1
            num_list = sorted(list(map(float, num_list)))                           # Create a sorted list from input
            std_length = len(num_list)                                              # Process to solve result
            a = sum(num_list) / std_length
            b = 0
            for i in num_list:
                b += (i - a) ** 2
            stdev = (b / (std_length - 1)) ** 0.5
            Label(root, text="Std is: " + str(stdev)).grid()                        # Show the result
            Label(root, text="Did you get the same answer?").grid()                 # Tell user to select if they do it correctly
            Button(root, text="Yes", command=yes).grid()                            # Display a "Yes" button
            Button(root, text="No", command=no).grid()                              # Display a "No" button
    except:                                                                         # Exception when value gets error
        Label(root, text="Please Enter Appropriate Values.").grid()


def calc_variance():                                                                # Function to calculate variance
    try:
        num_list = (numlist.get()).split(',')                                       # Split numbers from number list
        i = 0                                                                       # Initialize i for loop
        while i < len(num_list) - 1:
            if float(num_list[i]) < 0:                                              # Prevent number less than 0
                Label(root, text="Please enter numbers greater than 0.").grid()     # Tell user to input a number greater than 0
                flag = 0                                                            # Change flag to 0
                break                                                               # Break the loop
            else:
                flag = 1                                                            # Change flag to 1
            i += 1                                                                  # Increase i
        if flag == 1:                                                               # When flag = 1
            num_list = sorted(list(map(float, num_list)))                           # Create a sorted list from input
            mean = 0                                                                # Process to solve result
            for i in num_list:
                mean += i
            mean = mean / len(num_list)
            s1 = 0
            for i in num_list:
                s1 += (i - mean) ** 2
            var = s1 / (len(num_list) - 1)
            Label(root, text="Variance is: " + str(var)).grid()                     # Show the result
            Label(root, text="Did you get the same answer?").grid()                 # Tell user to select if they do it correctly
            Button(root, text="Yes", command=yes).grid()                            # Display a "Yes" button
            Button(root, text="No", command=no).grid()                              # Display a "No" button
    except:                                                                         # Exception when value gets error
        Label(root, text="Please Enter Appropriate Values.").grid()


def yes():                                                                          # This is correct word list
    yes_i = int(random.randint(0, 2))                                               # Use random to assign an integer to "yes_i"
    yes_list = ["Correct!", "Brilliant!", "Outstanding!"]                           # Fill "yes_list" with three word
    Label(root, text=yes_list[yes_i]).grid()                                        # Choose word randomly


def no():                                                                           # This is wrong word list
    no_i=int(random.randint(0, 2))                                                  # Use random to assign an integer to "no_i"
    no_list=["Try again.", "Wrong answer.", "It is a pity."]                        # Fill "no_list" with three word
    Label(root, text=no_list[no_i]).grid()                                          # Choose word randomly


root = Tk()                                                                         # Extend Tk to "root"
root.title("Mean, Median, Mode, Std, Variance")                                     # This is title

Label(root, text="Input numbers (Use ',' to separate): ").grid(row=0)               # Tell user to input numbers
numlist = Entry(root)                                                               # Make an input to input numvers
numlist.grid(row=0, column=1)                                                       # Position of input area

b1 = Button(root, text="Mean", bg="#ff9966", command=calc_mean)                     # Button to execute calc_mean function
b1.grid(row=1, column=0)                                                            # Position of the button
b2 = Button(root, text="Median", bg="#99ff88", command=calc_median)                 # Button to execute calc_median function
b2.grid(row=1, column=1)                                                            # Position of the button
b3 = Button(root, text="Mode", bg="#66bbff", command=calc_mode)                     # Button to execute calc_mode function
b3.grid(row=2, column=0)                                                            # Position of the button
b4 = Button(root, text="Std", bg="#ff99ee", command=calc_std)                       # Button to execute calc_std function
b4.grid(row=2, column=1)                                                            # Position of the button
b4 = Button(root, text="Variance", bg="#ffee22", command=calc_variance)             # Button to execute calc_variance function
b4.grid(row=3, column=0)                                                            # Position of the button
b5 = Button(root, text="Quit", bg="White", command=root.destroy)                    # Button to quit from program
b5.grid(row=3, column=1)                                                            # Position of the button

root.mainloop()                                                                     # Tkinter loop
