from tkinter import *

screen = Tk()
screen.title("VALORANT")
screen.config(bg="black")
screen.geometry("500x500")

#Component
text = Label(screen,text="Welcome to VALORANT",font=("Aeriel",20,"bold"), bg='black',fg='White')
text.pack()

name = Entry(screen,font=("Aeriel",12,"bold"),)
name.pack()

def Hello():
    print(f"Hello {name.get()}!")
    

mybutton = Button(screen,text="Click Me",font=("Aeriel",12,"bold"),bg='white',fg='black',command=Hello)
mybutton.pack()











screen.mainloop()