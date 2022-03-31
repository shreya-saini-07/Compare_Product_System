  #==================reset password=======================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Test@123",database="mydata")
            my_cursor=conn_cursor()
            query=("Select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cusor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, please login with new password",parent=self.root2)
                self.root2.destroy()

      #==================forgot pasword=================================
    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Plaese Enter the Email address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Test®123", database="mydata")
            my_cursor = conn.cursor()
            query =("select * from register where email=%s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)

            if row == None:
                messagebox.showerror("My Error", "Plaese enter the valid user name")

            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font="times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Friend Name","Your pet name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)


                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=370,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman,15"))
                self.txt_security.place(x=370,y=270,width=250)


                new_password=Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white",fg="black")
                new_password.place(x=370, y=150)

                self.txt_newpass = ttk.Entry(self.root2, font=("times new roman,15"))
                self.txt_newpass.place(x=370, y=270, width=250)

                btn=Button(self.root2,text"Reset",font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)





















