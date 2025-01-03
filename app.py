from tkinter import *

screen = Tk()
screen.title("My App")
screen.geometry("400x400")
screen.config(bg='lightgreen',)

#Frame
myframe = Frame(screen,height=50,width=400,bg="green")
myframe.pack()

#Label
mytext = Label(screen,text="Welcome to My App",font=("Times",20,"bold"),fg='white',bg='lightgreen')
mytext.pack()

first = Label(screen,text="Enter your name:",font=("Times",15,"bold"),fg='grey',bg='lightgreen')
first.pack()

name = Entry(screen,font=("Aeriel",12,"bold"))
name.pack()

enterage = Label(screen,text="Enter your age:",font=("Times",15,"bold"),fg='grey',bg='lightgreen')
enterage.pack()

age = Entry(screen,font=("Aeriel",12,"bold"))
age.pack()

empty = Label(bg='lightgreen')
empty.pack()

def buttonclick():
    myage = int(age.get())
    if myage >= 18:
        result.config(text="You are eligible for a driver's liscence.",fg='green',bg='lightgreen')
    else:
        result.config(text="You are ineligible for a driver's liscence",fg='red',bg='lightgreen')


submit = Button(screen,text="SUBMIT",font=("Arial",10,"bold"),fg='white',bg='black',padx=3,pady=2,command=buttonclick)
submit.pack()

result = Label(screen,font=("Times",18,"bold"),fg='white',bg='lightgreen')
result.pack()



screen.mainloop()