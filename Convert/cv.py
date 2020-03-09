from tkinter import *                                                                               # Tkinter (GUI) imported
import random                                                                                       # random to choose word
import math                                                                                         # math to convert different val


class Application(Frame):                                                                           # Extend methods from Frame
    globalnumber = 1


def kilo_to_mile():                                                                                 # Convert Kilometers to Miles
    try:                                                                                            # Try if value is right
        kilo = float(num.get())                                                                     # Get number from num and assign to "kilo" variable
        if kilo == 0:                                                                               # If "kilo" equals 0
            mile = 0
        else:                                                                                       # If "kilo" does not equals to 0
            mile = kilo * 0.621371                                                                  # Convert kilometers to miles
        Label(root, text=str(kilo)+"kilometers is equal to "+str('%.2f'%mile)+"mile.").grid()       # Show convert result
        Label(root, text="Do you make it right?").grid()                                            # Ask user if they do it correctly
        Button(root, text="Yes", command=rightword).grid()                                          # Create "Yes" button
        Button(root, text="No", command=wrongword).grid()                                           # Create "No" button
    except:                                                                                         # Throw exception
        Label(root, text="Please Enter Appropriate Values.").grid()


def c_to_f():                                                                                       # Convert Celsius Temperture to Fahrenheit Temperture
    try:                                                                                            # Try if value is right
        c = float(num.get())                                                                    	# Get number from num and assign to "c" variable
        if c < -273.15:                                                                         	# If "c" is lower than -273.15
            Label(root, text="Please Enter Appropriate Values.").grid()                             # Tell user to enter a new number
        else:                                                                                       # If "c" is not lower than -273.15
            f = (c * 1.8) + 32                                                              		# Convert Celsius to Fahrenheit
        Label(root, text=str(c)+"℃ is equal to "+str('%.2f'%f)+"℉.").grid()               		# Show convert result
        Label(root, text="Do you make it right?").grid()                                            # Ask user if they do it correctly
        Button(root, text="Yes", command=rightword).grid()                                          # Create "Yes" button
        Button(root, text="No", command=wrongword).grid()                                           # Create "No" button
    except:                                                                                         # Throw exception
        Label(root, text="Please Enter Appropriate Values.").grid()


def deg_to_rad():                                                                                   # Convert Degrees to rads
    try:                                                                                            # Try if value is right
        deg = float(num.get())                                                                   	# Get number from num and assign to "deg" variable
        rad = math.rads(deg)                                                               			# Math convert Degrees to Radians
        Label(root, text=str(deg)+"° is equal to "+str('%.2f'%rad)+"rad.").grid()             		# Show convert result
        Label(root, text="Do you make it right?").grid()                                            # Ask user if they do it correctly
        Button(root, text="Yes", command=rightword).grid()                                          # Create "Yes" button
        Button(root, text="No", command=wrongword).grid()                                           # Create "No" button
    except:                                                                                         # Throw exception
        Label(root, text="Please Enter Appropriate Values.").grid()


def right():                                                                                        # Convert right word list
    rightword = int(random.randint(0, 2))                                                           # Use random to assign an integer to "rightword"
    rightwordlist = ["Nice job!", "Correct!", "Good One!"]                                          # Fill "rightwordlist" with three word
    Label(root, text=rightwordlist[rightword]).grid()                                               # Choose word randomly


def wrong():                                                                                        # Convert wrong word list
    wrongword = int(random.randint(0, 2))                                                           # Use random to assign an integer to "wrongword"
    wrongwordlist = ["What a pity.", "Wrong.", "It must be something wrong"]                        # Fill "wrongwordlist" with three word
    Label(root, text=wrongwordlist[wrongword]).grid()                                               # Choose word randomly

root = Tk()                                                                                         # Extend Tk to "root"
root.title("Convert Multiple Variable")                                                             # title For root
Label(root, text="Input the value you want to convert:").grid(row=0)                                # Guide user to input number
num = Entry(root)                                                                                   # Input area to input number
num.grid(row=0, column=1)                                                                           # Position of input area
btn1 = Button(root, text="km to mi", bg="#E2B41C", command=kilo_to_mile)                            # Create Button 1
btn1.grid(row=1, column=0)                                                                          # Position of Button 1
btn2 = Button(root, text="℃ to ℉", bg="#76a4e5", command=c_to_f)                          		# Create Button 2
btn2.grid(row=1, column=1)                                                                          # Position of Button 2
btn3 = Button(root, text="° to rad", bg="#1adf12", command=deg_to_rad)                              # Create Button 3
btn3.grid(row=2, column=0)                                                                          # Position of Button 3
btn_quit = Button(root, text="Quit", bg="White", command=root.destroy)                              # Create Quit Button
btn_quit.grid(row=2, column=1)                                                                      # Position of the Quit Button
root.mainloop()                                                                                     # Tkinter loop