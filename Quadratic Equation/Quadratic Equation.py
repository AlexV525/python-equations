from tkinter import *                                                                                                       # Import tkinter for GUI.
import random                                                                                                               # Import ramdom for wordlist control.
import cmath                                                                                                                # Import cmath for calculate roots of the equation.


class Application(Frame):                                                                                                   # Create a show widget.
    globalnumber = 1                                                                                                        # Extend number scope to the whole program.
    

def quadratic():                                                                                                            # Quadratic subroutine to calculate the answer
    try:
        a = float(ea.get())                                                                                                 # Get a from ea.
        b = float(eb.get())                                                                                                 # Get b from eb.
        c = float(ec.get())                                                                                                 # Get c from ec.
        delta = (b**2) - (4*a*c)                                                                                            # Define the equation basic form.
        if delta == 0:                                                                                                      # When the equation has only one root.
            disc_root = cmath.sqrt(delta)                                                                                   # Use Complex Math to solve the equation.
            x1 = (-b-disc_root) / (2*a)                                                                                     # Assign the value to x1.
            Label(root, text="Only root for the equation is: "+str(x1)+".").grid()                                          # Display the result.
            Label(root, text="Is your answer right?").grid()                                                                # Create a label asks if you get the same answer.
            Button(root, text="Yes", command=correct).grid()                                                                # Create a button "Yes" and output correct_word list.
            Button(root, text="No", command=wrong).grid()                                                                   # Create a button "No" and outupt wrong_word list.

        else:                                                                                                               # When the equation has two roots.
            disc_root = cmath.sqrt(delta)                                                                                   # Use Complex Math to solve the equation.
            x1 = (-b-disc_root) / (2*a)                                                                                     # Assign the value to x1.
            x2 = (-b+disc_root) / (2*a)                                                                                     # Assign the value to x2.
            Label(root, text="Roots for the equation are: " + str(x1) + " and " + str(x2) + ".").grid()                     # Display the result.
            Label(root, text="Is your answer right?").grid()                                                                # Create a label asks if you get the same answer.
            Button(root, text="Yes", command=correct).grid()                                                                # Create a button "Yes" and output correct_word list.
            Button(root, text="No", command=wrong).grid()                                                                   # Create a button "No" and outupt wrong_word list.
    except:
        Label(root, text="Please Enter Appropriate Values").grid()

def correct():                                                                                                              # Create a correct word function.
    correct_word = int(random.randint(0, 2))                                                                                # Use random to choose a word in the wordlist.
    correct_wordlist = ["Great!", "Very good!", "Excellent!"]                                                               # Create a list to store three comments.
    Label(root, text=correct_wordlist[correct_word]).grid()                                                                 # Create a label to output the word that is randomly chose in the wordlist.


def wrong():                                                                                                                # Create a wrong word function.
    wrong_word=int(random.randint(0, 2))                                                                                    # Use random to choose a word in the wordlist.
    wrong_wordlist=["Keep tying.", "Check your calculation carefully.", "It must be wrong in your calculation somewhere."]  # Create a list to store three comments.
    Label(root, text=wrong_wordlist[wrong_word]).grid()                                                                     # Create a label to output the word that is randomly chose in the wordlist.


root = Tk()                                                                                                                 # Make a show widget.
root.title("Solve Quadratic Equation")                                                                                      # Define the title.
 
Label(root, text="Please enter coefficient a: ").grid(row=0)                                                                # Create a label in order to tell users input a.
ea = Entry(root)                                                                                                            # ea is assigned by what users input.
ea.grid(row=0, column=1)                                                                                                    # Show the position of the textbox.

Label(root, text="Please enter coefficient b: ").grid(row=1)                                                                # Create a label in order to tell users input b.
eb = Entry(root)                                                                                                            # eb is assigned by what users input.
eb.grid(row=1, column=1)                                                                                                    # Show the position of the textbox.

Label(root, text="Please enter coefficient c: ").grid(row=2)                                                                # Create a label in order to tell users input c.
ec = Entry(root)                                                                                                            # ec is assigned by what users input.
ec.grid(row=2, column=1)                                                                                                    # Show the position of the textbox.

b1 = Button(root, text="Solve", bg="#aaffaa", command=quadratic)                                                              # Create a button to trigger the solve process.
b1.grid(row=3, column=0)                                                                                                    # Show the button b1.
b2 = Button(root, text="Quit", bg="#ffaaaa", command=root.destroy)                                                              # Create a button to destory the widget and quit.
b2.grid(row=3, column=1)                                                                                                    # Show the button b2.

root.mainloop()                                                                                                             # Start looping.
