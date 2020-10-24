from tkinter import*
import tkinter.messagebox

class GUI_Beginners:

    def __init__(self,root):
        self.root = root
        self.root.title("Addition")
        self.root.geometry("1200x600")

        frame1 = Frame(self.root)
        frame1.grid()

        frame2 = Frame(self.root)
        frame2.grid(row = 0,column = 0)

        frame3 = Frame(frame1)
        frame3.grid(row=1,column = 0)

        FirstNum = StringVar()
        SecondNum = StringVar()

        self.lblFirstNum = Label(frame1,text="Enter First Number")
        self.lblFirstNum.grid(row=0,column=0)
        self.txtFirstNum = Entry(frame1,textvariable=FirstNum)
        self.txtFirstNum.grid(row=0,column=1)

        self.lblFirstNum = Label(frame1, text="Enter Second Number")
        self.lblFirstNum.grid(row=1, column=0)
        self.txtFirstNum = Entry(frame1, textvariable=SecondNum)
        self.txtFirstNum.grid(row=1, column=1)

        self.btnTotal = Button(frame3,text = 'Total')






if __name__=="__main__":
    root = Tk()
    application = GUI_Beginners
    root.mainloop()

