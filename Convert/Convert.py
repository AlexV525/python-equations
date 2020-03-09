from tkinter import *                                                                               # Tkinter (GUI) imported
import random                                                                                       # random to choose word
import math                                                                                         # math to convert radian


class Application(Frame):                                                                           # Extend methods from Frame
    globalnumber = 1


def km_to_mile():                                                                                   # This is Kilometers to Miles
    try:                                                                                            # Try if value is right
        kms = float(num.get())                                                                      # Get number from num and assign to "kms" variable
        if kms == 0:                                                                                # If "kms" equals 0
            miles = 0
        else:                                                                                       # If "kms" does not equals to 0
            miles = kms * 0.621371                                                                  # Convert kilometers to miles
        Label(root, text=str('%.2f'%kms)+"km is equal to "+str('%.2f'%miles)+"miles.").grid()       # Render the result with some words
        Label(root, text="Do you convert it right?").grid()                                         # Make user to select if they do it correctly
        Button(root, text="Yes", command=yesword).grid()                                            # Make a "Yes" button
        Button(root, text="No", command=noword).grid()                                              # Make a "No" button
    except:                                                                                         # Exception when value gets error
        Label(root, text="Please Enter Appropriate Values.").grid()


def ctemp_to_ftemp():                                                                               # This is Celsius to Fahrenheit
    try:                                                                                            # Try if value is right
        ctemp = float(num.get())                                                                    # Get number from num and assign to "ctemp" variable
        if ctemp < -273.15:                                                                         # If "ctemp" is lower than -273.15 (The lowest is -273.15 on the earth)
            Label(root, text="Nothing is cooler than -273.15℃.").grid()                            # Tell user to enter a new number
        else:                                                                                       # If "ctemp" is not lower than -273.15
            ftemp = (ctemp * 1.8) + 32                                                              # Convert Celsius to Fahrenheit
        Label(root, text=str('%.2f'%ctemp)+"℃ is equal to "+str('%.2f'%ftemp)+"℉.").grid()        # Render the result with some words
        Label(root, text="Do you convert it right?").grid()                                         # Make user to select if they do it correctly
        Button(root, text="Yes", command=yesword).grid()                                            # Make a "Yes" button
        Button(root, text="No", command=noword).grid()                                              # Make a "No" button
    except:                                                                                         # Exception when value gets error
        Label(root, text="Please Enter Appropriate Values.").grid()


def dg_to_rd():                                                                                     # This is Degrees to Radians
    try:                                                                                            # Try if value is right
        dgs = float(num.get())                                                                      # Get number from num and assign to "dgs" variable
        rds = math.radians(dgs)                                                                     # Math convert degrees to radians
        Label(root, text=str('%.2f'%dgs)+"° is equal to "+str('%.2f'%rds)+"rad.").grid()            # Render the result with some words
        Label(root, text="Do you convert it right?").grid()                                         # Make user to select if they do it correctly
        Button(root, text="Yes", command=yesword).grid()                                            # Make a "Yes" button
        Button(root, text="No", command=noword).grid()                                              # Make a "No" button
    except:                                                                                         # Exception when value gets error
        Label(root, text="Please Enter Appropriate Values.").grid()


def yesword():                                                                                      # This is right word list
    yes_word = int(random.randint(0, 2))                                                            # Use random to assign an integer to "yesword"
    yes_wordlist = ["Very good!", "Perfect!", "Wonderful!"]                                                               # Fill "yes_wordlist" with three word
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
btn1 = Button(root, text="km to mi", bg="#ea891c", command=km_to_mile)                              # Convert Kilometer to Miles Button
btn1.grid(row=1, column=0)                                                                          # Position of Button
btn2 = Button(root, text="℃ to ℉", bg="#1adf12", command=ctemp_to_ftemp)                          # Convert Celsius to Fahrenheit Button
btn2.grid(row=1, column=1)                                                                          # Position of Button
btn3 = Button(root, text="° to rad", bg="#76a4e5", command=dg_to_rd)                                # Convert Degree to Radius
btn3.grid(row=2, column=0)                                                                          # Position of Button                                                                        # Position of Button
btn_quit = Button(root, text="Quit", bg="White", command=root.destroy)                              # Quit Button
btn_quit.grid(row=2, column=1)                                                                      # Position of Button
root.mainloop()                                                                                     # Tkinter loop