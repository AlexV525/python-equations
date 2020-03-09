from tkinter import *     #Input graphical user interface
import math     #Input math function
import random     #Input random function
class Application(Frame):     #Create a show widget
 globalnumber=1     #Extend number scope to the whole program

def addition():     #Create a additive function
    number1=float(e1.get())     #Get the number from e1
    number2=float(e2.get())     #Get the number from e2
    number3=float(e3.get())     #Get the number from e3
    number4=float(e4.get())     #Get the number from e4
    number5=number1+number2+number3+number4     #Run the additive formula
    Label(root,text=number5).grid()     #Display the result number5
    Label(root,text="Do you get the same answer?").grid()     #Create a label asks if you get the same answer
    Button(root,text="Yes",command=correct_word).grid()     #Create a button"Yes" and output correct_word list
    Button(root,text="No",command=wrong_word).grid()     #Create a button"No" and output wrong_word list

def subtraction():     #Create a subtractive formula
    number1=float(e5.get())     #Get the number from e5
    number2=float(e6.get())     #Get the number from e6
    number3=number1-number2     #Run the subtractive formula
    while number3 ==int:     #If users type an integer number
        try:     #Create a try statement
            return number3     #Output number3
        except:     #If try statement is not satisfieded,then it will run the except statement
            return Label(root,text="Please type an integer!").grid()     #Display the text
    else:     #If while statement is not satisfieded,it will run the else statement
        number3=number1-number2     #Run the subtractive formula
        Label(root,text=number3).grid()     #Dislay the result number3
        Label(root,text="Do you get the same answer?").grid()     #Display a label asks if you get the same answer
        Button(root,text="Yes",command=correct_word).grid()     #Create a button"Yes" and output correct_Word list
        Button(root,text="No",command=wrong_word).grid()     #Create a button"No" and output wrong_word list

def multiplication():     #Create a multiplicative formula
    number1=float(e5.get())     #Get the number from e5
    number2=float(e6.get())     #Get the number from e6
    number3=number1*number2     #Run the multiplicative formula
    Label(root,text=number3).grid()     #Display a label asks if you get the same answer
    Label(root,text="Do you get the same answer?").grid()     #Display a label asks if you get the same answer
    Button(root,text="Yes",command=correct_word).grid()     #Create a button"Yes" and output correct_word list
    Button(root,text="No",command=wrong_word).grid()     #Create a button"No" and output wrong_word list

def division():     #Create a divisional formula
    number1=float(e5.get())     #Get the number from e5
    number2=float(e6.get())     #Get the number from e6
    if number2==0:     #If users enter 0
        try:     #Create a try statement
            return number1/number2     #Output number1 divided by number2
        except:     #If try statement is not satisfieded,then it will run the except statement
             return Label(root,text="Denominator can not be 0.Please type a new number!").grid()     #Display a label
    else:     #If while statement is not satisfieded,it will run the else statement
         number3=number1/number2     #Run the divisional formula
         Label(root,text=number3).grid()
         Label(root,text="Do you get the same answer?").grid()     #Display a label asks if you get the same answer
         Button(root,text="Yes",command=correct_word).grid()     #Create a button"Yes" and output correct_word list
         Button(root,text="No",command=wrong_word).grid()     #Create a button"No" and output wrong_word list

def correct_word():     #Create a correct word function
    word=int(random.randint(0,2))     #Use random function to choose one in the wordlist
    wordlist=["Awesome!","Well done!","Good job!"]     #Create a list to store three comments
    Label(root,text=wordlist[word]).grid()     #Create a label to output the word that is randomly chose in the wordlist

def wrong_word():     #Create a wrong word function
    word1=int(random.randint(0,2))     #Use random function to choose one in the wordlist1
    wordlist1=["What a pity,it's wrong.","Don't give up!Do it again.","Something wrong in your calcuation."]     #Create a list to store three comments
    Label(root,text=wordlist1[word1]).grid()     #Create a label to output the word that is randomly chose in the wordlist

root=Tk()     #Make a show widget
root.title("Simple Calculator")     #Give the program a title
Label(root,text="Input a number1").grid(row=0)     #Create a label in order to tell users input a number1
Label(root,text="Input a number2").grid(row=1)     #Create a label in order to tell users input a number2
Label(root,text="Input a number3").grid(row=2)     #Create a label in order to tell users input a number3
Label(root,text="Input a number4").grid(row=3)     #Create a label in order to tell users input a number4
Label(root,text="Input a number5").grid(row=5)     #Create a label in order to tell users input a number5
Label(root,text="Input a number6").grid(row=6)     #Create a label in order to tell users input a number6
e1=Entry(root)     #e1 is assigned by what users input
e1.grid(row=0,column=1)     #Show the position of the textbox
e2=Entry(root)     #e2 is assigned by what users input
e2.grid(row=1,column=1)     #Show the position of the textbox
e3=Entry(root)     #e3 is assigned by what users input
e3.grid(row=2,column=1)     #Show the position of the textbox
e4=Entry(root)     #e4 is assigned by what users input
e4.grid(row=3,column=1)     #Show the position of the textbox
e5=Entry(root)     #e5 is assigned by what users input
e5.grid(row=5,column=1)     #Show the position of the textbox
e6=Entry(root)     #e6 is assigned by what users input
e6.grid(row=6,column=1)     #Show the position of the textbox
b1=Button(root,text="Add",bg="Red",command=addition).grid(row=4,column=1)     #Create a button with red colour and run the addition function at row4,column1
b2=Button(root,text="Subtract",bg="Yellow",command=subtraction).grid(row=7,column=0)     #Create a button with yellow colour and run the subtract function at row7,column0
b3=Button(root,text="Multiply",bg="Green",command=multiplication).grid(row=7,column=1)     #Create a button with green colour and run the multiply function at row7,column1
b4=Button(root,text="Divide",bg="Blue",command=division).grid(row=7,column=2)     #Create a button with blue colour and run the divide function at row7,column2
root.mainloop()     #Start looping



