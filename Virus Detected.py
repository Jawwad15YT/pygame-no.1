from tkinter import *
from tkinter import messagebox
import random

screen = Tk()
screen.config(bg='lightblue')
screen.title("Virus Scanner")
screen.geometry("300x300")

viruslist = [True,False]

virus = random.choice(viruslist)

header = Label(screen,text='Check your device if its safe or not?',bg='lightblue',fg='blue',font=("Arial",10,"bold"))
header.pack()

waste = Label(screen,bg='lightblue')
waste.pack()

def ScanVirus():
    virus = random.choice(viruslist)
    if (virus == True):
        messagebox.showwarning("Virus detected!!!", "urgently get an antivirus software!!")
    elif (virus == False):
        messagebox.showinfo("Your device is safe","The free antivirus is working as intended.")



Check = Button(screen,text='Check.',fg='darkblue',font=("Arial",10,"bold"),command=ScanVirus)
Check.pack()










screen.mainloop()