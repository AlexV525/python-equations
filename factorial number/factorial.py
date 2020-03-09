from tkinter import *                                                                       # import Tkinter for GUI
import random                                                                               # import random function for random words.


class Application(Frame):                                                                   # Create a show widget.
    globalnumber = 1                                                                        # Extend number scope to the whole program.


def factorial():                                                                            # Define a factorial function.
    try:
        num = n1.get()                                                                      # Get value from n1
        if num.isdigit():                                                                   # Judge value type
            num = int(num)                                                                  # Convert value to integer
            factorial_num = 1                                                               # Start factorial from 1
            i = 1
            while i < num:                                                                  # Make a loop
                i = i + 1
                factorial_num = factorial_num * i
            Label(root, text="Factorial number is: " + str(factorial_num) + ".").grid()     # Display the result.
            Label(root, text="Did you get the right answer?").grid()                        # Create a label asks if you get the correct answer.
            Button(root, text="Yes", command=correct).grid()                                # Create a button "Yes" and output c_word list.
            Button(root, text="No", command=wrong).grid()                                   # Create a button "No" and outupt w_word list.
        else:                                                                               # If input is not a integer.
            Label(root, text="Please Enter an integer.").grid()                             # Display the tip.
    except:                                                                                 # Exception handler.
        Label(root, text="Please Enter Appropriate Values.").grid()                         # Display the tip.


def correct():                                                                              # Define a correct word function.
    c_word = int(random.randint(0, 2))                                                      # Use random to choose a word in the wordlist.
    c_wordlist = ["You did great!", "Keep your precision!", "Wonderful!"]                   # Create a list to store three comments.
    Label(root, text=c_wordlist[c_word]).grid()                                             # Create a label to output the word that is randomly chose in the wordlist.


def wrong():                                                                                # Define a wrong word function.
    w_word = int(random.randint(0, 2))                                                      # Use random to choose a word in the wordlist.
    w_wordlist = ["Sorry, try again.", "You should do it again.", "Wrong answer."]          # Create a list to store three comments.
    Label(root, text=w_wordlist[w_word]).grid()                                             # Create a label to output the word that is randomly chose in the wordlist.


root = Tk()                                                                                 # Make a show widget.
root.title("Factorial")                                                                     # Define the title.

Label(root, text="Input an integer: ").grid(row=0)                                          # Create a label in order to tell users to input integer.
n1 = Entry(root)                                                                            # n1 is assigned by what users input.
n1.grid(row=0, column=1)                                                                    # Show the position of the textbox.

b1 = Button(root, text="Factorial", bg="Red", command=factorial)                            # Create a button to trigger the factorial process.
b1.grid(row=1, column=0)                                                                    # Show the button b1.
b2 = Button(root, text="Quit", bg="Yellow", command=root.destroy)                           # Create a button to destory the widget and quit.
b2.grid(row=1, column=1)                                                                    # Show the button b5.

root.mainloop()                                                                             # Start looping.