from tkinter import *                                                                               # Tkinter (GUI) imported
import random                                                                                       # random to choose word


class Application(Frame):                                                                           # Extend methods from Frame
    globalnumber = 1


def dec_to_bin():                                                                                   # This is Decimal to Binary
    try:                                                                                            # Try if value is right
        decimal = float(num.get())                                                                  # Get number from num and assign to "decimal" variable
        if decimal == 0:                                                                            # If "decimal" equals 0
            binary = 0b0
        else:                                                                                       # If "decimal" does not equals to 0
            binary = bin(decimal)                                                                   # Convert Decimal to Binary
        Label(root, text=str(decimal)+" is: "+str(binary)+"in binary.").grid()                      # Render the result with some words
        Label(root, text="Do you convert it right?").grid()                                         # Make user to select if they do it correctly
        Button(root, text="Yes", command=yesword).grid()                                            # Make a "Yes" button
        Button(root, text="No", command=noword).grid()                                              # Make a "No" button
    except:                                                                                         # Exception when value gets error
        Label(root, text="Please Enter Appropriate Values.").grid()


def dec_to_oct():                                                                                   # This is Decimal to Octal
    try:                                                                                            # Try if value is right
        decimal = float(num.get())                                                                  # Get number from num and assign to "decimal" variable
        if decimal == 0:                                                                            # If "decimal" equals 0
            octal = 0o0
        else:                                                                                       # If "decimal" does not equals to 0
            octal = oct(decimal)                                                                    # Convert Decimal to Pctal
        Label(root, text=str(decimal)+" is: "+str(octal)+"in octal.").grid()                        # Render the result with some words
        Label(root, text="Do you convert it right?").grid()                                         # Make user to select if they do it correctly
        Button(root, text="Yes", command=yesword).grid()                                            # Make a "Yes" button
        Button(root, text="No", command=noword).grid()                                              # Make a "No" button
    except:                                                                                         # Exception when value gets error
        Label(root, text="Please Enter Appropriate Values.").grid()


def dec_to_hex():                                                                                   # This is Decimal to Hexadecimal
    try:                                                                                            # Try if value is right
        if decimal == 0:                                                                            # If "decimal" equald to 0
            hexadecimal = 0x0
        else:                                                                                       # If "decimal" does not equal to 0
            hexadecimal = hex(decimal)                                                              # Convert Decimal to Hexadecimal
        Label(root, text=str(decimal)+" is: "+str(hexadecimal)+"in hexadecimal.").grid()            # Render the result with some words
        Label(root, text="Do you convert it right?").grid()                                         # Make user to select if they do it correctly
        Button(root, text="Yes", command=yesword).grid()                                            # Make a "Yes" button
        Button(root, text="No", command=noword).grid()                                              # Make a "No" button
    except:                                                                                         # Exception when value gets error
        Label(root, text="Please Enter Appropriate Values.").grid()


def yesword():                                                                                      # This is right word list
    yes_word = int(random.randint(0, 2))                                                            # Use random to assign an integer to "yesword"
    yes_wordlist = ["Very good!", "Perfect!", "Wonderful!"]                                         # Fill "yes_wordlist" with three word
    Label(root, text=yes_wordlist[yes_word]).grid()                                                 # Choose word randomly


def noword():                                                                                       # This is wrong word list
    no_word = int(random.randint(0, 2))                                                             # Use random to assign an integer to "noword"
    no_wordlist = ["Try again.", "Wrong answer.", "Do it again."]                                   # Fill "no_wordlist" with three word
    Label(root, text=no_wordlist[no_word]).grid()                                                   # Choose word randomly

root = Tk()                                                                                         # Extend Tk to "root"
root.title("Convert")                                                                               # This is title
Label(root, text="Input a number you want to convert:").grid(row=0)                                 # Guide user to input number
num = Entry(root)                                                                                   # Input area to input number
num.grid(row=0, column=1)                                                                           # Position of input area
btn1 = Button(root, text="DEC→BIN", bg="#ea891c", command=dec_to_bin)                               # Convert Decimal to Binary Button
btn1.grid(row=1, column=0)                                                                          # Position of Button
btn2 = Button(root, text="DEC→OC", bg="#1adf12", command=dec_to_oct)                                # Convert Decimal to Octal Button
btn2.grid(row=1, column=1)                                                                          # Position of Button
btn3 = Button(root, text="DEC→HEX", bg="#76a4e5", command=dec_to_hex)                               # Convert Decimal to Hexadecimal Button
btn3.grid(row=2, column=0)                                                                          # Position of Button                                                                        # Position of Button
btn_quit = Button(root, text="Quit", bg="White", command=root.destroy)                              # Quit Button
btn_quit.grid(row=2, column=1)                                                                      # Position of Button
root.mainloop()                                                                                     # Tkinter loop