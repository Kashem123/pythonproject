from tkinter import *


root = Tk()
root.title("Bangladesh Information")
root.geometry("600x400+0+0")

Button1 = Button(root,text="Bangladesh",font=("Arial",30,"bold"),pady=20,padx=30,bd=10,bg="green")
Button1.grid(row=0,column=0)

Button1 = Button(root,text="Chittagong",font=("Arial",30,"bold"),pady=20,padx=30,bd=10,bg="green")
Button1.grid(row=0,column=1)

Button1 = Button(root,text="Sylet",font=("Arial",30,"bold"),pady=20,padx=30,bd=10,bg="green")
Button1.grid(row=1,column=1)



root.mainloop()

class Information:
    def __init__(self, Dhaka, Chittagong, Rajshai, Borisal, Sylet, Khulna, Rangpur):
        self.Dhaka = Dhaka
        self.Chittagong = Chittagong
        self.Rajshai = Rajshai
        self.Borisal = Borisal
        self.Sylet = Sylet
        self.Khulna = Khulna
        self.Rangpur = Rangpur
    
    def Button_click(self):
        print("my click")
        


