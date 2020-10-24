from tkinter import *
y = ""
x = 2
player_1 = []
player_2 = []

def define_sign(number):
    global x,y
    global player_1,player_2

    if number == 1:
        if x%2 == 0:
            y = "x"
            player_1.append(number)
            print(player_1)
        elif x%2 != 0:
            y = "0"
            player_2.append(number)
            print(player_2)
class con_fig():
    def __init__(self,b1,b2,b3,b4,b5,b6,b7,b8,b9):
        self.b1=b1.config(test=y)
        self.b2=b2.config(test=y)
        self.b3=b3.config(test=y)
        self.b4=b4.config(test=y)
        self.b5=b5.config(test=y)
        self.b6=b6.config(test=y)
        self.b7=b7.config(test=y)
        self.b8=b8.config(test=y)
        self.b9=b9.config(test=y)

root = Tk()
li = Label(root,text="player 1 : x",font="times 15")
li.grid(row=0,column=2)

b1 = Button(root,bg="red",width=20,height=10,command=lambda : define_sign(1))
b1.grid(row=1,column=1)

b2 = Button(root,bg="black",width=20,height=10,command=lambda : define_sign(2))
b2.grid(row=1,column=2)

b3 = Button(root,bg="green",width=20,height=10,command=lambda : define_sign(3))
b3.grid(row=1,column=3)

b4 = Button(root,bg="yellow",width=20,height=10,command=lambda : define_sign(4))
b4.grid(row=4,column=1)

b5 = Button(root,bg="pink",width=20,height=10,command=lambda : define_sign(5))
b5.grid(row=4,column=2)

b6 = Button(root,bg="tomato",width=20,height=10,command=lambda : define_sign(6))
b6.grid(row=4,column=3)

b7 = Button(root,bg="blue",width=20,height=10,command=lambda : define_sign(7))
b7.grid(row=8,column=1)

b8 = Button(root,bg="black",width=20,height=10,command=lambda : define_sign(8))
b8.grid(row=8,column=2)

b9 = Button(root,bg="red",width=20,height=10,command=lambda : define_sign(9))
b9.grid(row=8,column=3)

root.mainloop()