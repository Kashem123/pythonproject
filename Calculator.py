from tkinter import*

def btnclick (numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sum_up=str(eval(operator))
    text_Input.set(sum_up)
    operator=""

root = Tk()
root.geometry("360x447")
root.resizable(0,0)
root.title("Calculator")
operator=""
text_Input =StringVar()

txtDisplay = Entry(root,font=('arial',20,'bold'), textvariable=text_Input, bd=30,insertwidth=4,
                   bg="red",justify='right').grid(columnspan=4)

btu7=Button(root,padx=24,pady=18,bd=8, fg="black",font=('arial',20,'bold'),
            text="7",bg="red",command=lambda:btnclick(7)).grid(row=1,column=0)

btu8=Button(root,padx=24,pady=18,bd=8, fg="black",font=('arial',20,'bold'),
            text="8",bg="red",command=lambda:btnclick(8)).grid(row=1,column=1)

btu9=Button(root,padx=24,pady=18,bd=8, fg="black",font=('arial',20,'bold'),
            text="9",bg="red",command=lambda:btnclick(9)).grid(row=1,column=2)

Addition=Button(root,padx=24,pady=18,bd=8, fg="black",font=('arial',20,'bold'),
            text="+",bg="red",command=lambda:btnclick("+")).grid(row=1,column=3)
#==========================================================================
btn4=Button(root,padx=24,pady=18,bd=8, fg="black",font=('arial',20,'bold'),
            text="4",bg="red",command=lambda:btnclick(4)).grid(row=2,column=0)

btn5=Button(root,padx=24,pady=18,bd=8, fg="black",font=('arial',20,'bold'),
            text="5",bg="red",command=lambda:btnclick(5)).grid(row=2,column=1)

btn6=Button(root,padx=24,pady=18,bd=8, fg="black",font=('arial',20,'bold'),
            text="6",bg="red",command=lambda:btnclick(6)).grid(row=2,column=2)

Subtraction=Button(root,padx=24,pady=18,bd=8, fg="black",font=('arial',20,'bold'),
            text="-",bg="red",command=lambda:btnclick("-")).grid(row=2,column=3)
#==========================================================================
btn1=Button(root,padx=24,pady=18,bd=8, fg="black",font=('arial',20,'bold'),
            text="1",bg="red",command=lambda:btnclick(1)).grid(row=3,column=0)

btn2=Button(root,padx=24,pady=18,bd=8, fg="black",font=('arial',20,'bold'),
            text="2",bg="red",command=lambda:btnclick(2)).grid(row=3,column=1)

btn3=Button(root,padx=24,pady=18,bd=8, fg="black",font=('arial',20,'bold'),
            text="3",bg="red",command=lambda:btnclick(3)).grid(row=3,column=2)

Multiply=Button(root,padx=24,pady=18,bd=8, fg="black",font=('arial',20,'bold'),
            text="*",bg="red",command=lambda:btnclick("*")).grid(row=3,column=3)
#==========================================================================
btn0=Button(root,padx=24,pady=18,bd=8, fg="black",font=('arial',20,'bold'),
            text="0",bg="red",command=lambda:btnclick(0)).grid(row=4,column=0)

btnClear=Button(root,padx=24,pady=18,bd=8, fg="black",font=('arial',20,'bold'),
            text="C",bg="red",command=btnClearDisplay).grid(row=4,column=1)

btnEquals=Button(root,padx=24,pady=18,bd=8, fg="black",font=('arial',20,'bold'),
            text="=",bg="red",command=btnEqualsInput).grid(row=4,column=2)

Division=Button(root,padx=24,pady=18,bd=8, fg="black",font=('arial',20,'bold'),
            text="/",bg="red",command=lambda:btnclick("/")).grid(row=4,column=3)

root.mainloop()














    
