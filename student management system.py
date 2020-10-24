from  tkinter import *
from tkinter import ttk

class Student():
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1370x700+0+0")

        titel = Label(self.root,text="Student Management System",bd=9,relief=GROOVE,font=("times new roman",50,"bold"),bg="yellow",fg="red")
        titel.pack(side=TOP,fill=X)

        #===========ManageFrame=======
        Manage_Frame = Frame(self.root,bd=6,relief=RIDGE,bg="blue")
        Manage_Frame.place(x=20,y=100,width=458,height=585)

        m_title = Label(Manage_Frame,text="Manage Student",bg="yellow",fg="black",font=("times new roman",40,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll = Label(Manage_Frame, text="Roll No:", bg="yellow", fg="black",font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1, column=0,pady=10,padx=20,sticky="w")
        tex_Roll = Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        tex_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name = Label(Manage_Frame, text="Name:", bg="yellow", fg="black", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10,padx=20, sticky="w")
        tex_Name = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        tex_Name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_email = Label(Manage_Frame, text="Email:", bg="yellow", fg="black", font=("times new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=10,padx=20, sticky="w")
        tex_Email = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        tex_Email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(Manage_Frame, text="Gender:", bg="yellow", fg="black", font=("times new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10,padx=20, sticky="w")
        combo_gender = ttk.Combobox(Manage_Frame,font=("lines new roman",13,"bold"),state="readonly")
        combo_gender["values"] = ("male","female","other")
        combo_gender.grid(row=4,column=1,pady=10,padx=20)

        lbl_contact = Label(Manage_Frame, text="Contact:", bg="yellow", fg="black", font=("times new roman", 20, "bold"))
        lbl_contact.grid(row=5, column=0, pady=10,padx=20, sticky="w")
        tex_Contact = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        tex_Contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_dob = Label(Manage_Frame, text="D.O.B:", bg="yellow", fg="black", font=("times new roman", 20, "bold"))
        lbl_dob.grid(row=6, column=0,pady=10, padx=20, sticky="w")
        tex_Dob = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        tex_Dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_address = Label(Manage_Frame, text="Address:", bg="yellow", fg="black", font=("times new roman", 20, "bold"))
        lbl_address.grid(row=7, column=0, pady=10,padx=20, sticky="w")
        self.tex_Address = Text(Manage_Frame,width=30,height=3,font=("times new roman", 10, "bold"))
        self.tex_Address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        #=========Button frame========
        btn_frame = Frame(Manage_Frame,bd=3,relief=RIDGE,bg="black")
        btn_frame.place(x=10,y=525,width=420)

        Add_btn = Button(btn_frame,text="Add",width=7).grid(row=0,column=0,padx=10,pady=10)
        Update_btn = Button(btn_frame,text="Update",width=7).grid(row=0, column=1, padx=10, pady=10)
        Delete_btn = Button(btn_frame,text="Delete",width=7).grid(row=0, column=2, padx=10, pady=10)
        Clear_btn = Button(btn_frame,text="Clear",width=7).grid(row=0, column=3, padx=10, pady=10)

        Details_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="blue")
        Details_Frame.place(x=500, y=100, width=880, height=585)

        lbl_search = Label(Details_Frame, text="Search By", bg="yellow", fg="black",
                           font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        combo_search = ttk.Combobox(Details_Frame, font=("lines new roman", 13, "bold"), width=10, state="readonly")
        combo_search["values"] = ("Roll_no", "Name", "Contact", "other")
        combo_search.grid(row=0, column=1, pady=10, padx=20)
        tex_search = Entry(Details_Frame, font=("times new roman", 10, "bold"), width=20, bd=5, relief=GROOVE)
        tex_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(Details_Frame,text="Search",width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
        showallbtn = Button(Details_Frame,text="Show All",width=10,pady=5).grid(row=0,column=4,padx=10,pady=10)

        # ===========TableFrame=======
        Table_Frame = Frame(Details_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=760, height=500)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.Student_table = ttk.Treeview(Table_Frame,column=("roll", "name", "email", "gender", "contact", "dob", "address"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("roll",text="Roll No")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("dob", text="D.O.B")
        self.Student_table.heading("address", text="Address")

        self.Student_table["show"]="headings"
        self.Student_table.column("roll", width=100)
        self.Student_table.column("name", width=100)
        self.Student_table.column("email", width=100)
        self.Student_table.column("gender", width=100)
        self.Student_table.column("contact", width=100)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("address", width=150)

        self.Student_table.pack(fill=BOTH, expand=1)


class Student():
    pass
    root = Tk()
    obj = Student(root)
    root.mainloop()
