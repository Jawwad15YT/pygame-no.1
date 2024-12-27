from tkinter import *

window = Tk()
window.title("Age Calculator")
window.config(bg="Lightblue")
window.geometry("250x250")
window.iconbitmap("original.ico")

header = Frame(window,height=30,width=250,bg='navy')
header.pack_propagate(False)
header.pack()
Welcome = Label(header,text="Welcome to Age Calculator",font=("Ariel",13,"bold"),fg="white",bg="navy")
Welcome.pack()

AgeLabel = Label(window,text="Enter Your Birth Year",font=("Times",13,"bold"),fg="Black",bg="LightBlue")
AgeLabel.pack()

AgeInput = Entry(window,font=("Aeriel",14,"bold"))
AgeInput.pack()

Label(window,bg="LightBlue").pack()

def CalculateAge():
    BY = AgeInput.get()
    if int(BY) < 2024:
        age = 2024 - int(BY)
        Result.config(text=f"You are {age} years old",fg="green")
    else:
        Result.config(text='Invalid Age',fg="red")
    

Calculate = Button(window,text="Calculate Age",bg='black',fg='white',padx=3,pady=2,font=("Ariel",12,"bold"),command=CalculateAge)
Calculate.pack()

Label(window,bg="LightBlue").pack()

Result = Label(window,bg='lightblue',fg='green',font=("Aeriel",14,"bold"))
Result.pack()


window.mainloop()