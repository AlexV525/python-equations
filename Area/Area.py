from tkinter import *                                                                   # Tkinter for GUI
import random                                                                           # random for random words.


class Application(Frame):                                                               # Create a show widget.
    globalnumber = 1                                                                    # Extend number scope to the whole program.


def area_of_triangle():                                                                 # Define a triangle area function.
    try:
        a = float(n1.get())                                                             # Get float number from n1
        b = float(n2.get())                                                             # Get float number from n2
        c = float(n3.get())                                                             # Get float number from n3
        if a == 0 or b == 0 or c == 0:                                                  # If user enter 0.
            Label(root, text="Please enter a new number.").grid()
        else:
            p = ( a + b + c ) / 2                                                       # Calculate semi-perimeter
            s = ( p * ( p - a ) * ( p - b ) * ( p - c ) ) ** 0.5                        # Calculate the area of triangle
            Label(root, text="The Area of your triangle is: "+str('%.2f'%s)+".").grid() # Display the result.
            Label(root, text="Is your answer correct?").grid()                          # Ask if user get the correct answer.
            Button(root, text="Yes", command=right).grid()                              # Create "Yes" button
            Button(root, text="No", command=wrong).grid()                               # Create "No" button
    except:                                                                             # Throw exception
        Label(root, text="Please Enter Appropriate Values.").grid()


def area_of_rectangle():                                                                # Define a rectangle area function.
    try:
        a = float(n1.get())                                                             # Get float number from n1
        b = float(n2.get())                                                             # Get float number from n2
        if a == 0 or b == 0:                                                            # If user enter 0.
            Label(root, text="Please enter a new number.").grid()
        else:
            s = a * b                                                                   # Calculate the area of rectangle
            Label(root, text="The Area of your rectangle is: "+str('%.2f'%s)+".").grid()# Display the result.
            Label(root, text="Is your answer correct?").grid()                          # Ask if user get the correct answer.
            Button(root, text="Yes", command=right).grid()                              # Create "Yes" button
            Button(root, text="No", command=wrong).grid()                               # Create "No" button
    except:                                                                             # Throw exception
        Label(root, text="Please Enter Appropriate Values.").grid()


def area_of_circle():                                                                   # Define a triangle area function.
    try:
        r = float(n1.get())                                                             # Get float number from n1
        if r == 0:                                                                      # If user enter 0.
            Label(root, text="Please enter a new number.").grid()
        else:
            pi = 3.141592653589793
            s = pi * (r ** 2)                                                           # Calculate the area of circle
            Label(root, text="The Area of your circle is: "+str('%.2f'%s)+".").grid()   # Display the result.
            Label(root, text="Is your answer correct?").grid()                          # Ask if user get the correct answer.
            Button(root, text="Yes", command=right).grid()                              # Create "Yes" button
            Button(root, text="No", command=wrong).grid()                               # Create "No" button
    except:                                                                             # Throw exception
        Label(root, text="Please Enter Appropriate Values.").grid()


def area_of_trapezoid():                                                                # Define a trapezoid area function.
    try:
        b1 = float(n1.get())                                                            # Get float number from n1
        b2 = float(n2.get())                                                            # Get float number from n2
        h = float(n3.get())                                                             # Get float number from n3
        if b1 == 0 or b2 == 0 or h == 0:                                                # If user enter 0.
            Label(root, text="Please enter a new number.").grid()
        else:
            s = ( h * ( b1 + b2 ) ) / 2                                                 # Calculate the area of trapezoid
            Label(root, text="The Area of your trapezoid is: "+str('%.2f'%s)+".").grid()# Display the result.
            Label(root, text="Is your answer correct?").grid()                          # Ask if user get the correct answer.
            Button(root, text="Yes", command=right).grid()                              # Create "Yes" button
            Button(root, text="No", command=wrong).grid()                               # Create "No" button
    except:                                                                             # Throw exception
        Label(root, text="Please Enter Appropriate Values.").grid()


def right():                                                                            # Define a right word list
    rightword = int(random.randint(0, 2))                                               # Use random to assign an integer to "rightword"
    rightwordlist = ["Nice job!", "Correct!", "Good One!"]                              # Fill "rightwordlist" with three word
    Label(root, text=rightwordlist[rightword]).grid()                                   # Choose a word randomly


def wrong():                                                                            # Define a wrong word list
    wrongword = int(random.randint(0, 2))                                               # Use random to assign an integer to "wrongword"
    wrongwordlist = ["What a pity.", "Wrong.", "It must be something wrong"]            # Fill "wrongwordlist" with three word
    Label(root, text=wrongwordlist[wrongword]).grid()                                   # Choose a word randomly


root = Tk()                                                                             # Make a show widget.
root.title("Calculate Area")                                                            # Define the title.

Label(root, text="Input number 1: ").grid(row=0)                                        # User input number 1.
n1 = Entry(root)                                                                        # n1 is assigned by what users input.
n1.grid(row=0, column=1)                                                                # Show the position of the textbox.
Label(root, text="(Square/Triangle's \"a\", Circle's \"r\", Trapezoid's \"b1\")").grid(row=1)
Label(root, text="Input number 2: ").grid(row=2)                                        # User input number 2.
n2 = Entry(root)                                                                        # n2 is assigned by what users input.
n2.grid(row=2, column=1)                                                                # Show the position of the textbox.
Label(root, text="(Square/Triangle's \"b\", Trapezoid's \"b2\")").grid(row=3)
Label(root, text="Input number 3: ").grid(row=4)                                        # User input number 3.
n3 = Entry(root)                                                                        # n3 is assigned by what users input.
n3.grid(row=4, column=1)                                                                # Show the position of the textbox.
Label(root, text="(Triangle's \"c\", Trapezoid's \"h\")").grid(row=5)

b1 = Button(root, text="Triangle", bg="#40E0D0", command=area_of_triangle)              # Button to trigger the triangle process.
b1.grid(row=6, column=0)                                                                # Show the button b1.
b2 = Button(root, text="Rectangle", bg="#FFA500", command=area_of_rectangle)            # Button to trigger the rectangle root process.
b2.grid(row=6, column=1)                                                                # Show the button b2.
b3 = Button(root, text="Circle", bg="#FF6347", command=area_of_circle)                  # Button to trigger the circle process.
b3.grid(row=7, column=0)                                                                # Show the button b3.
b4 = Button(root, text="Trapezoid", bg="#00FF7F", command=area_of_trapezoid)            # Button to trigger the trapezoid root process.
b4.grid(row=7, column=1)                                                                # Show the button b4.
b5 = Button(root, text="Quit", bg="White", command=root.destroy)                        # Button to destory the widget and quit.
b5.grid(row=8, column=0)                                                                # Show the button b5.

root.mainloop()                                                                         # Start looping.
