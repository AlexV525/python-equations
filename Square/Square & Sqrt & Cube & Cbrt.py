from tkinter import *                                                                   # Tkinter for GUI
import random                                                                           # random for random words.


class Application(Frame):                                                               # Create a show widget.
    globalnumber = 1                                                                    # Extend number scope to the whole program.


def square():                                                                           # Define a square function.
    try:
        num = float(n1.get())                                                           # Get float number from n1
        if num == 0:                                                                    # If user enter 0.
            Label(root, text="Please enter a new number.").grid()
        else:
            square_result = num ** 2                                                    # Calculate square result
            Label(root, text="Square result is: "+str(square_result)+".").grid()        # Display the result.
            Label(root, text="Is your answer correct?").grid()                          # Asks if user get the correct answer.
            Button(root, text="Yes", command=praise).grid()                             # Button "Yes" and output a word from correct_wordlist.
            Button(root, text="No", command=inflate).grid()                             # Button "No" and output a word from wrong_wordlist.
    except ValueError:
        Label(root, text="Please Enter Appropriate Values.").grid()


def square_rt():                                                                        # Define a square root function.
    try:
        num = float(n1.get())                                                           # Get float number from n1
        if num == 0:                                                                    # If user enter 0.
            Label(root, text="Please enter a new number.").grid()
        else:
            square_rt_result = num ** 0.5                                               # Calculate square root result
            Label(root, text="The square root is: "+str(square_rt_result)+".").grid()   # Display the result.
            Label(root, text="Is your answer correct?").grid()                          # Asks if user get the correct answer.
            Button(root, text="Yes", command=praise).grid()                             # Button "Yes" and output a word from correct_wordlist.
            Button(root, text="No", command=inflate).grid()                             # Button "No" and output a word from wrong_wordlist.
    except ValueError:
        Label(root, text="Please Enter Appropriate Values.").grid()


def cube():                                                                             # Define a cube function.
    try:
        num = float(n1.get())                                                           # Get float number from n1
        if num == 0:                                                                    # If user enter 0.
            Label(root, text="Please enter a new number.").grid()
        else:
            cube_result = num ** 3                                                      # Calculate cube result
            Label(root, text="The cube is: "+str(cube_result)+".").grid()               # Display the result.
            Label(root, text="Is your answer correct?").grid()                          # Asks if user get the correct answer.
            Button(root, text="Yes", command=praise).grid()                             # Button "Yes" and output a word from correct_wordlist.
            Button(root, text="No", command=inflate).grid()                             # Button "No" and output a word from wrong_wordlist.
    except ValueError:
        Label(root, text="Please Enter Appropriate Values.").grid()


def cube_rt():                                                                          # Define a cube root function.
    try:
        num = float(n1.get())                                                           # Get float number from n1
        if num == 0:                                                                    # If user enter 0.
            Label(root, text="Please enter a new number.").grid()
        else:
            cube_rt_result = num ** (1.0/3)                                             # Calculate cube root result
            Label(root, text="The cube root is :"+str(cube_rt_result)+".").grid()
            Label(root, text="Is your answer correct?").grid()                          # Asks if user get the correct answer.
            Button(root, text="Yes", command=praise).grid()                             # Button "Yes" and output a word from correct_wordlist.
            Button(root, text="No", command=inflate).grid()                             # Button "No" and output a word from wrong_wordlist.
    except ValueError:
        Label(root, text="Please Enter Appropriate Values.").grid()


def praise():                                                                           # Define a correct word function.
    correct_word = int(random.randint(0, 2))                                            # Use random to choose a word in the wordlist.
    correct_wordlist = ["You done well!", "Perfect!", "Good job!"]                      # A list to store three comments.
    Label(root, text=correct_wordlist[correct_word]).grid()                             # A label to output the word that is randomly chose in the wordlist.


def inflate():                                                                          # Define a wrong word function.
    wrong_word = int(random.randint(0, 2))                                              # Use random to choose a word in the wordlist.
    wrong_wordlist = ["Do it again.", "Keep going.", "Wrong calculation maybe."]        # A list to store three comments.
    Label(root, text=wrong_wordlist[wrong_word]).grid()                                 # A label to output the word that is randomly chose in the wordlist.


root = Tk()                                                                             # Make a show widget.
root.title("Square & Sqrt & Cube & Cbrt")                                               # Define the title.

Label(root, text="Input number: ").grid(row=0)                                          # User input number.
n1 = Entry(root)                                                                        # n1 is assigned by what users input.
n1.grid(row=0, column=1)                                                                # Show the position of the textbox.

b1 = Button(root, text="Square", bg="#40E0D0", command=square)                          # Button to trigger the square process.
b1.grid(row=2, column=0)                                                                # Show the button b1.
b2 = Button(root, text="Square Root", bg="#FFA500", command=square_rt)                  # Button to trigger the square root process.
b2.grid(row=2, column=1)                                                                # Show the button b2.
b3 = Button(root, text="Cube", bg="#FF6347", command=cube)                              # Button to trigger the cube process.
b3.grid(row=3, column=0)                                                                # Show the button b3.
b4 = Button(root, text="Cube Root", bg="#00FF7F", command=cube_rt)                      # Button to trigger the cube root process.
b4.grid(row=3, column=1)                                                                # Show the button b4.
b5 = Button(root, text="Quit", bg="White", command=root.destroy)                        # Button to destory the widget and quit.
b5.grid(row=4, column=0)                                                                # Show the button b5.

root.mainloop()                                                                         # Start looping.
