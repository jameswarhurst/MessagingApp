from tkinter import *
from tkinter import ttk

def welcomePage():
    window = Tk()
    wlclbl=Label(window, text="WELCOME TO SMS", fg='green', font=("Helvetica", 20))
    wlclbl.place(x=50, y=20)

    btn=Button(window, text="Login", fg='red', command=login)
    btn.place(x=120, y=85)

    btn=Button(window, text="Sign up", fg='red',command=signup)
    btn.place(x=115, y=125)

    window.configure(bg='black')
    window.title('Homepage')
    window.geometry("300x200+10+10")
    window.mainloop()

def login():
    def login_button_click():
        user = usrfld.get()
        passw = pasfld.get()
        window.destroy()

        with open("users.txt", "r") as file:
            data = file.read()
        lines = data.split("\n")

        for line in lines:
            if line != "":
                saved_user, saved_pass = line.split(":")
                if user == saved_user and passw == saved_pass:
                    homepage()
                    return

        print("Wrong login")

    window=Tk()

    btn=Button(window, text="Ok", fg='red', command=login_button_click)
    btn.place(x=210, y=105)

    lbl=Label(window, text="Enter Your Username", fg='blue', font=("Helvetica", 16))
    lbl.place(x=10, y=20)

    lbl1=Label(window, text="Enter Your Password", fg='green', font=("Helvetica", 16))
    lbl1.place(x=10, y=80)

    usrfld=Entry(window, bd=5)
    usrfld.place(x=10, y=45)

    pasfld=Entry(window, bd=5, show="*")
    pasfld.place(x=10, y=105)

    window.title('Login Page')
    window.geometry("300x200+10+10")
    window.mainloop()

def signup():
    def signup_button_click():
        newuser = usrfld.get()
        newuserpass = pasfld.get()
        window.destroy()

        with open("users.txt", "r+") as file:
            data = file.read()
            if f"{newuser}:{newuserpass}" not in data:
                file.write(f"\n{newuser}:{newuserpass}")

        login()

    window = Tk()

    btn=Button(window, text="Ok", fg='red', command=signup_button_click)
    btn.place(x=210, y=105)

    lbl=Label(window, text="Enter A Username", fg='blue', font=("Helvetica", 16))
    lbl.place(x=10, y=20)

    lbl1=Label(window, text="Enter A Password", fg='green', font=("Helvetica", 16))
    lbl1.place(x=10, y=80)

    usrfld=Entry(window, bd=5)
    usrfld.place(x=10, y=45)

    pasfld=Entry(window, bd=5, show="*")
    pasfld.place(x=10, y=105)

    window.title('Sign Up Page')
    window.geometry("300x200+10+10")
    window.mainloop()

def homepage():
    window = Tk()

    succesfullbl = Label(window, text="Successful login, welcome back" , fg='green', font=("Helvetica", 20))
    succesfullbl.place(x=30, y=30)
    
    window.title('SUCCESSFUL LOGIN')
    window.geometry("300x200+10+10")
    window.mainloop()

welcomePage()