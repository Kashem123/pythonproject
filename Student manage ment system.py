from tkinter import *
from tkinter import ttk

class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        title = Label(self.root,text="Student Management System",font=("times new roman",40,"bold"),bg="yellow",bd=10,relief=GROOVE)
        title.pack(side=TOP,fill=X)
        #===========All variable==========
        self.Roll_No_var = StringVar()
        self.Name_var = StringVar()
        self.Email_var = StringVar()
        self.Gender_var = StringVar()
        self.Contact_var = StringVar()
        self.Dob_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        #=========Manage Frame============
        Manage_Frame = Frame(self.root, bd=6, relief=RIDGE, bg="crimson")
        Manage_Frame.place(x=20, y=100, width=458, height=585)

        m_title = Label(Manage_Frame,bg="crimson",fg="white",text="Manage Students",font=("times new roman",15,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll = Label(Manage_Frame,text="Roll No :",bg="crimson",fg="white",font=("times new roman",15,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        txt_Roll = Entry(Manage_Frame,textvariable= self.Roll_No_var ,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name = Label(Manage_Frame,text="Name    :", bg="crimson", fg="white", font=("times new roman", 15, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_Name = Entry(Manage_Frame,textvariable=self.Name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_email = Label(Manage_Frame,text="Email    :", bg="crimson", fg="white", font=("times new roman", 15, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_Email = Entry(Manage_Frame,textvariable=self.Email_var , font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(Manage_Frame, text="Gender :", bg="crimson", fg="white", font=("times new roman", 15, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        combo_Gender=ttk.Combobox(Manage_Frame,textvariable=self.Gender_var,font=("lines new roman",13,"bold"))
        combo_Gender["values"]=("Male","Female","Other")
        combo_Gender.grid(row=4,column=1,pady=10,padx=20)

        lbl_contact = Label(Manage_Frame,text="Contact :", bg="crimson", fg="white", font=("times new roman", 15, "bold"))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        txt_Contact = Entry(Manage_Frame,textvariable= self.Contact_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_dob= Label(Manage_Frame,text="D.O.B    :", bg="crimson", fg="white", font=("times new roman", 15, "bold"))
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        txt_Dob = Entry(Manage_Frame, textvariable= self.Dob_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_address = Label(Manage_Frame, text="Address :", bg="crimson", fg="white", font=("times new roman", 15, "bold"))
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        txt_Address = Text(Manage_Frame,width=20,height=2, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        #========Button Frame===========
        btn_frame = Frame(Manage_Frame, bd=3, relief=RIDGE, bg="black")
        btn_frame.place(x=10, y=500, width=420)

        Add_btn = Button(btn_frame, text="Add", width=7).grid(row=0, column=0, padx=10, pady=10)
        Update_btn = Button(btn_frame, text="Update", width=7).grid(row=0, column=1, padx=10, pady=10)
        Delete_btn = Button(btn_frame, text="Delete", width=7).grid(row=0, column=2, padx=10, pady=10)
        Clear_btn = Button(btn_frame, text="Clear", width=7).grid(row=0, column=3, padx=10,pady=10)

        #============Detail Frame==============

        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=500, y=100, width=780, height=585)

        lbl_search = Label(Detail_Frame, text="Search By", bg="yellow", fg="black",font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.search_by, font=("lines new roman", 13, "bold"), width=10, state="readonly")
        combo_search["values"] = ("Roll_no", "Name", "Contact", "other")
        combo_search.grid(row=0, column=1, pady=10, padx=20)
        tex_search = Entry(Detail_Frame,textvariable=self.search_txt, font=("times new roman", 10, "bold"), width=20, bd=5, relief=GROOVE)
        tex_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(Detail_Frame, text="Search", width=10, pady=5).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(Detail_Frame, text="Show All", width=8, pady=5).grid(row=0, column=4, padx=10, pady=10)

        #=========Table Frame============

        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=760, height=500)

        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)
        Student_Table = ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=Student_Table.xview)
        scroll_y.config(command=Student_Table.yview)
        Student_Table.heading("roll",text="Roll No.")
        Student_Table.heading("name", text="Name.")
        Student_Table.heading("email", text="Email.")
        Student_Table.heading("gender", text="Gender.")
        Student_Table.heading("contact", text="Contact.")
        Student_Table.heading("dob", text="D.O.B.")
        Student_Table.heading("address", text="Address.")
        Student_Table["show"]="headings"
        Student_Table.column("roll",width=100)
        Student_Table.column("name", width=100)
        Student_Table.column("email", width=100)
        Student_Table.column("gender", width=100)
        Student_Table.column("contact", width=100)
        Student_Table.column("dob", width=100)
        Student_Table.column("address", width=100)
        Student_Table.pack(fill=BOTH,expand=1)





root=Tk()
ob = Student(root)
root.mainloop()



