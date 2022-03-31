import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Login_Window:
    def __init__(self, root) :
        self.root = root
        self.root.title("LOGIN")
        self.root.geometry("1550x800+0+0")

        #background image
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Vineet\Pictures\a.jpg")
        lbl_bg = tkinter.Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        #frame
        frame= Frame (self.root,bg="black")
        frame.place(x=500,y=100,width=350,height=500)

        img1=Image.open(r"C:\Users\Vineet\Pictures\a.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lbl_img1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lbl_img1.place(x=630,y=110,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=110,y=120)

        #username field
        username=lbl=Label(frame,text="USERNAME",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=165)
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=200,width=270)

        #password field
        password = lbl = Label(frame, text="PASSWORD", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)
        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=260, width=270)

        #image username
        img2=Image.open(r"C:\Users\Vineet\Pictures\a.jpg")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimg2,bg="black",borderwidth=0)
        lblimg1.place(x=500,y=300,width=25,height=25)

        #image password
        img3=Image.open(r"C:\Users\Vineet\Pictures\a.jpg")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimg2,bg="black",borderwidth=0)
        lblimg1.place(x=500,y=300,width=25,height=25)

        #loginbutton
        loginbtn=Button(frame,text="Login",font=("times new roman", 15, "bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #registerbutton
        registerbtn = Button(frame, text="Sign In", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white",bg="red", activeforeground="white", activebackground="red")
        registerbtn.place(x=15, y=350, width=160, height=35)

        # forgetbutton
        forgetbtn = Button(frame, text="Forget Password", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white",bg="red", activeforeground="white", activebackground="red")
        forgetbtn.place(x=15, y=370, width=160, height=35)













































if __name__ == '__main__':
    root=tkinter.Tk()
    app=Login_Window(root)
    root.mainloop()
