from tkinter import*
from tkinter.messagebox import showinfo
y = ""
x = 2
player_1 = []
player_2 = []
def define_sign():
    global x,y
    global player_1,player_2

    if number == 1:
        if x%2==0:
            y = "x"
            player_1.append(number)
            print(player_1)
        elif x%2 != 0:
            y = "o"
            player_2.append(number)
            print(player_2)
        b1.config(text=y)
        x = x+1
root = tk()
        
l1 = Label(root,text="player 1 : x",font= "times 15")
l1.grid(row=0,column=1)

l2 = Label(root,text="player 2 : 0",font= "times 15")
l2.grid(row=0,column=2)

b1 = Button(root,width=20,height=10,command=lambda:define_sign(1))
b1.grid(row=1,column=1) 

b2 = Button(root,width=20,height=10,command=lambda:define_sign(2))
b2.grid(row=1,column=2) 

b3 = Button(root,width=20,height=10,command=lambda:define_sign(3))
b3.grid(row=1,column=3) 

b4 = Button(root,width=20,height=10,command=lambda:define_sign(4))
b4.grid(row=4,column=1)

b5 = Button(root,width=20,height=10,command=lambda:define_sign(5))
b5.grid(row=4,column=2) 

b6 = Button(root,width=20,height=10,command=lambda:define_sign(6))
b6.grid(row=4,column=3) 

b7 = Button(root,width=20,height=10,command=lambda:define_sign(7))
b7.grid(row=8,column=1) 

b8 = Button(root,width=20,height=10,command=lambda:define_sign(8))
b8.grid(row=8,column=2) 

b9 = Button(root,width=20,height=10,command=lambda:define_sign(9))
b9.grid(row=8,column=3) 

