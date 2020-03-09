from tkinter import *                                                               # Tkinter (GUI) imported
import random                                                                       # random to choose word


class Application(Frame):                                                           # Define a class to extend Frame
    globalnumber = 1


def leap_year():                                                                    # Define leap year function
    try:
        year = int(y.get())
        if year == 0:                                                               # If year is 0
            Label(root, text="Please enter a new number.").grid()                   # Tell user to input a new number
        else:                                                                       # If year is not 0
            if (year % 4) == 0:                                                     # Divide by 4
               if (year % 100) == 0:                                                # Divide by 100
                   if (year % 400) == 0:                                            # Divide by 400
                       Label(root, text=str(year)+" is a leap year.").grid()        # Display correct tip
                   else:
                       Label(root, text=str(year)+" is not a leap year.").grid()    # Display wrong tip
               else:
                   Label(root, text=str(year)+" is a leap year.").grid()            # Display correct tip
            else:
                Label(root, text=str(year)+" is not a leap year.").grid()           # Display wrong tip
        Label(root, text="Do you make it right?").grid()                            # Tell user to select if they do it correctly
        Button(root, text="Yes", command=yes).grid()                                # Display a "Yes" button
        Button(root, text="No", command=no).grid()                                  # Display a "No" button
    except:                                                                         # Exception when value gets error
        Label(root, text="Please Enter Appropriate Values.").grid()


def yes():                                                                          # This is correct word list
    yes_i = int(random.randint(0, 2))                                               # Use random to assign an integer to "yes_i"
    yes_list = ["Very good!", "Wonderful!", "Perfect!"]                             # Fill "yes_list" with three word
    Label(root, text=yes_list[yes_i]).grid()                                        # Choose word randomly


def no():                                                                           # This is wrong word list
    no_i = int(random.randint(0, 2))                                                # Use random to assign an integer to "no_i"
    no_list = ["Try again.", "Wrong answer.", "Do it again."]                       # Fill "no_list" with three word
    Label(root, text=no_list[no_i]).grid()                                          # Choose word randomly


root = Tk()                                                                         # Extend Tk to "root"
root.title("Leap Year")                                                             # This is title

Label(root, text="Input an year: ").grid(row=0)                                     # Tell user to input y
y = Entry(root)                                                                     # Make an input to input y
y.grid(row=0, column=1)                                                             # Position of input area
btn1 = Button(root, text="Leap Year", bg="#fa891c", command=leap_year)              # Calculate if it's leap year
btn1.grid(row=1, column=0)                                                          # Position of Button
btn2 = Button(root, text="Quit", bg="White", command=root.destroy)                  # Quit Button
btn2.grid(row=1, column=1)                                                          # Position of Button

root.mainloop()                                                                     # Tkinter loop