import re
import os
def choices():
    print("Please choose what you would like to do.")
    choice = int(input("1.Login , 2.Register , 3. Forget Password "))
    if choice == 1:
       return getdetails()
    elif choice == 2:
       return register_user()
    elif choice == 3:
       return forget_password()


def register_user():

    print("Password must contains one digit,one special character,one uppercase and one lowercase")
    name = str(input("Enter your Email Id: "))
    password = str(input("Enter Your Password: "))

    #global username_info = name
    #global password_info = password

    u = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    p = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.fullmatch(u, name) or re.fullmatch(p, password):
            print("Registration Success")
            file = open("username", "a")
            file.write("\n"+ name + "\t")
            file.write(password )
            file.close()

def getdetails():
    #print("Please Provide")
    global name
    global password

    name = str(input("Name: "))
    password = str(input("Password: "))

    with open("username", "r") as f:
        if name in f.read():
            print("Login Success")
        else:
            print("EmailId not found, please register")
            choices()

def forget_password():
        p1 = input("Enter your old password")
        with open("username", "r") as f:
            if p1 in f.read():
                password = str(input("Enter new password"))
                file = open("username", "a")
                file.write(password)
                file.close()
                print("your password has been changed")
            else:
                print("Invalid old password, please register")
                register_user()

choices()
