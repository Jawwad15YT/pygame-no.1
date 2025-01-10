from tkinter import *
import random

screen = Tk()
screen.geometry("250x300")
screen.title("The Number Guesser!")
screen.config(bg='lightblue')

Headframe = Frame(screen, width=300, height=50, bg="darkblue")
Headframe.pack(fill=X)

Text1 = Label(Headframe, text="Let the Number Guesser begin!", bg='darkblue', fg='white', font=("Times", 13, "bold"))
Text1.pack(pady=10)

l1 = Label(screen, text="Rule", bg='lightblue', fg='black', font=("Times", 10, "bold"))
l1.pack()

rule = Label(screen, text="You have to Guess the number \nWhich is decided by the computer. (1,10)", bg='lightblue', fg='darkred', font=("Times", 12, "bold"))
rule.pack()

l2 = Label(screen, text="Enter your number here:", bg='lightblue', fg='black', font=("Times", 11, "bold"))
l2.pack()

Numberinput = Entry(screen, bg='lightgrey', fg='black', font=("Times", 12, "bold"))
Numberinput.pack()

l3 = Label(screen, bg='lightblue')
l3.pack()

def RandomNumber():
    global computerNumber
    computerNumber = random.randint(1, 10)
    Numberinput.delete(0, END)
    #result.config(text="Game reset! Enter a new guess.", fg="blue")

RandomNumber()

def Solution():
    try:
        user_guess = int(Numberinput.get())
        if computerNumber == user_guess:
            result.config(fg='green', text="You Win!")
        else:
            result.config(fg='red', text="Guess Again")
    except ValueError:
        result.config(fg='orange', text="Please enter a valid number!")

check = Button(screen, text="Check!", bg='black', fg='white', font=("Times", 10, "bold"), command=Solution)
check.pack(side='right')

reset = Button(screen, text="Reset", bg='black', fg='white', font=("Times", 10, "bold"), command=RandomNumber)
reset.pack(side='left')

result = Label(screen, font=("Times", 11, "bold"), bg='lightblue')
result.pack()

screen.mainloop()
