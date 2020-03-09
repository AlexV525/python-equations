from tkinter import *
import random


class Application(Frame):                                                                               # Extend Frame's function
    globalnumber = 1


def division():
    try:                                                                                                # Try to get numbers from input
        num = int(n1.get())                                                                             # Get num from n1
        num_list_1 = int(nl1.get())                                                                     # Get num_list_1 from nl1
        num_list_2 = int(nl2.get())                                                                     # Get num_list_1 from nl2
        num_list_3 = int(nl3.get())                                                                     # Get num_list_1 from nl3
        num_list_4 = int(nl4.get())                                                                     # Get num_list_1 from nl4
        num_list_5 = int(nl5.get())                                                                     # Get num_list_1 from nl5
        if num == 0:                                                                                    # If x is 0
            Label(root, text="Please enter a new x.").grid()
        else:                                                                                           # If x is not 0
            num_list = [num_list_1, num_list_2, num_list_3, num_list_4, num_list_5]                     # Fill the number list
            dv_result = list(filter(lambda x: (x % num == 0), num_list))                                # Use lambda to find division number
            Label(root, text="Numbers divisible by " + str(num) + " are"+str(dv_result)+".").grid()     # Show the result
            Label(root, text="Did you get the same answer?").grid()                                     # Label show tips
            Button(root, text="Yes", command=correct).grid()                                            # Button "Yes"
            Button(root, text="No", command=wrong).grid()                                               # Button "No"
    except:
        Label(root, text="Please Enter Appropriate Values.").grid()                                     # Tell user re-enter a new value


def correct():                                                                                          # Function to show correct word
    correct_word = int(random.randint(0, 2))                                                            # Import random to choose word
    correct_wordlist = ["Perfect!", "Nice job!", "Well done!"]                                          # Make a word list
    Label(root, text=correct_wordlist[correct_word]).grid()                                             # Display word in grid


def wrong():                                                                                            # Function to show correct word
    wrong_word=int(random.randint(0, 2))                                                                # Import random to choose word
    wrong_wordlist=["Try again.", "Sorry.", "What a pity."]                                             # Make a word list
    Label(root, text=wrong_wordlist[wrong_word]).grid()                                                 # Display word in grid


root = Tk()                                                                                             # Assign Tkinter to root GUI
root.title("Divisible")                                                                                 # Title for GUI
Label(root, text="Input x: ").grid(row=0)                                                               # Display a label
n1 = Entry(root)                                                                                        # Make an input "n1"
n1.grid(row=0, column=1)                                                                                # "n1"'s position
Label(root, text="Input number 1 of list: ").grid(row=1)                                                # Display a label
nl1 = Entry(root)                                                                                       # Make an input "nl1"
nl1.grid(row=1, column=1)                                                                               # "nl1"'s position
Label(root, text="Input number 2 of list: ").grid(row=2)                                                # Display a label
nl2 = Entry(root)                                                                                       # Make an input "nl2"
nl2.grid(row=2, column=1)                                                                               # "nl2"'s position
Label(root, text="Input number 3 of list: ").grid(row=3)                                                # Display a label
nl3 = Entry(root)                                                                                       # Make an input "nl3"
nl3.grid(row=3, column=1)                                                                               # "nl3"'s position
Label(root, text="Input number 4 of list: ").grid(row=4)                                                # Display a label
nl4 = Entry(root)                                                                                       # Make an input "nl4"
nl4.grid(row=4, column=1)                                                                               # "nl4"'s position
Label(root, text="Input number 5 of list: ").grid(row=5)                                                # Display a label
nl5 = Entry(root)                                                                                       # Make an input "nl5"
nl5.grid(row=5, column=1)                                                                               # "nl5"'s position
b1 = Button(root, text="Find", bg="#52da56", command=division)                                          # Button "Find" and trigger division
b1.grid(row=6, column=0)                                                                                # "Find"'s position
b2 = Button(root, text="Quit", bg="White", command=root.destroy)                                        # Button "Quit" and trigger root.destroy
b2.grid(row=6, column=1)                                                                                # "Quit"'s position

root.mainloop()                                                                                         # Main Loop
