import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title ("Register")
        self.root.geometry("1600x900+0+0")

        self.var_fname=StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pswd = StringVar()
        self.var_confirmpswd = StringVar()
        self.var_check= IntVar()


        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Vineet\Pictures\a.jpg")
        bg_lbl1=Label(self.root, image=self.bg)
        bg_lbl1.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=250, y=50, width=830, height=600)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",24,"bold"),fg="white",bg="black")
        register_lbl.place(x=260,y=4)

        img1=Image.open(r"C:\Users\Vineet\Pictures\a.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lbl_img1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lbl_img1.place(x=620,y=90,width=60,height=60)

        fname_lbl=Label(frame,text="First Name",font=("times new roman",18,"bold"),fg="white",bg="black")
        fname_lbl.place(x=50,y=100)
        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",18,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        lname_lbl=Label(frame,text="Last Name",font=("times new roman",18,"bold"),fg="white",bg="black")
        lname_lbl.place(x=520,y=100)
        self.lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",18,"bold"))
        self.lname_entry.place(x=520,y=130,width=250)

        contact_lbl=Label(frame,text="Contact No.",font=("times new roman",18,"bold"),fg="white",bg="black")
        contact_lbl.place(x=50,y=200)
        self.contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",18,"bold"))
        self.contact_entry.place(x=50,y=230,width=250)

        email_lbl=Label(frame,text="Email ID.",font=("times new roman",18,"bold"),fg="white",bg="black")
        email_lbl.place(x=520,y=200)
        self.email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",18,"bold"))
        self.email_entry.place(x=520,y=230,width=250)

        securityQ_lbl=Label(frame,text="Security Question",font=("times new roman",18,"bold"),fg="white",bg="black")
        securityQ_lbl.place(x=50,y=300)
        self.combo_securityQ=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15),state="readonly")
        self.combo_securityQ["values"]=("Select","Your nickname","Your birth place","Your pet name")
        self.combo_securityQ.current(0)
        self.combo_securityQ.place(x=50,y=330,width=250)


        securityA_lbl=Label(frame,text="Security Answer",font=("times new roman",18,"bold"),fg="white",bg="black")
        securityA_lbl.place(x=520,y=300)
        self.securityA_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",18,"bold"))
        self.securityA_entry.place(x=520,y=330,width=250)

        pswd_lbl=Label(frame,text="Password",font=("times new roman",18,"bold"),fg="white",bg="black")
        pswd_lbl.place(x=50,y=400)
        self.pswd_entry=ttk.Entry(frame,textvariable=self.var_pswd,font=("times new roman",18,"bold"))
        self.pswd_entry.place(x=50,y=430,width=250)

        confirmpswd_lbl=Label(frame,text="Confirm Password",font=("times new roman",18,"bold"),fg="white",bg="black")
        confirmpswd_lbl.place(x=520,y=400)
        self.confirmpswd_entry=ttk.Entry(frame,textvariable=self.var_confirmpswd,font=("times new roman",18,"bold"))
        self.confirmpswd_entry.place(x=520,y=430,width=250)

        self.checkbtn=Checkbutton(frame,variable=self.var_check,activeforeground="black", activebackground="white",fg="black",text="I agree with Terms and Condition",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50, y=480)


        loginbtn = Button(frame, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white",bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=415, y=530, width=100, height=35)
        registerbtn = Button(frame,command=self.register_data, text="Register", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white",bg="red", activeforeground="white", activebackground="red")
        registerbtn.place(x=280, y=530, width=100, height=35)

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
                messagebox.showerror("Error","All fields required")
        elif self.var_pswd.get()!=self.var_confirmpswd.get():
                messagebox.showerror("Error", "Password and Confirm Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Agree to Terms and Condition")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="2004",database="project_class12")
            cur=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror("Error","Email already exists")
            else:
                cur.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(self.var_fname.get(),self.var_lname.get(),self.var_contact.get(),self.var_email.get(),self.var_securityQ.get(),self.var_securityA.get(),self.var_pswd.get()))
                messagebox.showinfo("Sucess", "Registration sucessfull")
            conn.commit()
            conn.close()




if __name__ == '__main__':
    root=tkinter.Tk()
    app=Register(root)
    root.mainloop()
