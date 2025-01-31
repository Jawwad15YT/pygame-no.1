from tkinter import *

screen = Tk()
screen.config(bg='pink')
screen.title("Restaurant")
screen.geometry("400x500")

header = Label(screen,width='500',height='60',bg='red')
header.pack(fill='x')

text = Label(header,text="Welcome to my restaurant!",bg='red',fg='white',font=("Arial",12,"bold"))
text.pack(pady='10')

menulabel = Label(screen,text="Here's the available menu",bg='pink',fg='red',font=("Arial",12,"bold"))
menulabel.pack()

pizzalabel = Label(screen,text="Pizza",fg="green",bg="pink",font=("Arial",15,"bold"))
pizzalabel.place(x=10,y=80)

pizzaq = Entry(font=("Arial",10,"bold"))
pizzaq.place(y=85,x=70)

burgerlabel = Label(screen,text="Burger",fg="green",bg='pink',font=("Arial",15,"bold"))
burgerlabel.place(x=10,y=115)

burgerq = Entry(font=("Arial",10,"bold"))
burgerq.place(y=120,x=85)

Order = Button(screen,text="Order",bg='red',fg='white',padx=12,pady=6,font=("Arial",12,"bold"))
Order.place(y=150,x=170)

Bill = Frame(screen,bg='white',height=200,width=200)
Bill.place(y=200,x=110)

Print = Button(screen,text="Print",bg='red',fg='white',padx=12,pady=6,font=("Arial",12,"bold"))
Print.place(y=410,x=170)

screen.mainloop()