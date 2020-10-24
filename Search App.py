from tkinter import *
from tkinter.scrolledtext import ScrolledText
import wikipedia as wiki

def search():
    search_data = ent.get()
    data = wiki.summary(search_data,sentences=8)
    ent.set('')
    text.delete(0.0,END)
    search_lbl["text"]="Searching result for :{}".format(search_data)
    text.insert(0.0,data)

def enter_pressed(event):
    search()

root = Tk()
root.title("Search Application")
root.geometry("320x480")
root.configure(bg="white")

ent = StringVar()

search_entry = Entry(root,width=25,font=("arial",12),bd=2,relief=RIDGE,textvariable=ent)
search_entry.bind("<Return>",enter_pressed)
search_entry.place(x=15,y=20)

search_lbl = Label(root,text="Searching result for : ",font=("arial",12,"bold"),bg="white")
search_lbl.place(x=15,y=70)

text = ScrolledText(root,font=("times",10),bd=4,relief=SUNKEN,wrap=WORD)
text.place(x=15,y=100,height=300,width=300)

search_btn = Button(root,text="search",font=("arial",12,"bold"),width=8,command=search)
search_btn.place(x=10,y=420)

clear_btn = Button(root,text="clear",font=("arial",12,"bold"),width=8,command=lambda :text.delete(0.0,END))
clear_btn.place(x=105,y=420)

exit_btn = Button(root,text="exit",font=("arial",12,"bold"),width=8,command=root.quit)
exit_btn.place(x=200,y=420)



root.mainloop()
