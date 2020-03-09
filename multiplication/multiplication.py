from tkinter import *                                                               # GUI module imported
import random                                                                       # Random module imported


class Application(Frame):                                                           # Make a widget
    globalnumber = 1


def multiply_table():                                                               # This is multiply table section
    try:
        num = int(n1.get())                                                         # Get integer number from n1
        if num == 0:                                                                # If user enter 0
            Label(root, text="0×n is meaningless.").grid()
        else:
            low_bound = int(lb.get())                                               # Get low bound from lb
            high_bound = int(hb.get())                                              # Get high bound from hb
            Label(root, text="Multiplication Table:").grid()                        # Show the table label
            for i in range(low_bound, high_bound+1):                                # Make a loop from low bound to high bound
                mt_result = num * i                                                 # Multiply action
                Label(root, text=str(num)+"×"+str(i)+"="+str(mt_result)).grid()     # Show the table
            Label(root, text="Is your multiplication correct?").grid()              # Answer confirmation
            Button(root, text="Yes", command=righttable).grid()                     # "Yes" Button
            Button(root, text="No", command=wrongtable).grid()                      # "No" Button
    except:
        Label(root, text="Please Enter Appropriate Values.").grid()


def righttable():                                                                   # Right words section
    rtable = int(random.randint(0, 2))                                              # Random module to select a word from list
    rtablelist = ["Correct!", "Good One!", "Well done!"]                            # Right words list
    Label(root, text=rtablelist[rtable]).grid()                                     # Show the word


def wrongtable():                                                                   # Wrong words section
    wtable = int(random.randint(0, 2))                                              # Random module to select a word from list
    wtablelist = ["Do it again.", "Sorry.", "Wrong."]                               # Wrong words list
    Label(root, text=wtablelist[wtable]).grid()                                     # Show the word


root = Tk()                                                                         # root widget
root.title("Multiplication Table")                                                  # root widget's title
Label(root, text="Input the Table number (Integer): ").grid(row=0)                  # Tell user to input the table number
n1 = Entry(root)                                                                    # Make user to input n1
n1.grid(row=0, column=1)                                                            # Position of input n1
Label(root, text="Input the Low bound (Integer): ").grid(row=1)                     # Tell user to input the low bound
lb = Entry(root)                                                                    # Make user to input lb
lb.grid(row=1, column=1)                                                            # Position of input lb
Label(root, text="Input the High bound (Integer): ").grid(row=2)                    # Tell user to input the high bound
hb = Entry(root)                                                                    # Make user to input hb
hb.grid(row=2, column=1)                                                            # Position of input hb
b1 = Button(root, text="Make Table", bg="#f44", command=multiply_table)             # Calculate button
b1.grid(row=3, column=0)                                                            # Position of the calculate button
b2 = Button(root, text="Quit", bg="#4f4", command=root.destroy)                     # Quit button
b2.grid(row=3, column=1)                                                            # Position of the quit button

root.mainloop()                                                                     # root widget looping
