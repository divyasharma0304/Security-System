#Importing Modules
 
from tkinter import *
import os


#Function for Setup Window
 
def setup():
    global setup_window
    setup_window = Toplevel(main_window)
    setup_window['bg']='#000000'
    setup_window.title("Set-Up")
    setup_window.geometry("500x400")
 
    global username
    global password
    global username_portal
    global password_portal
    username = StringVar()
    password = StringVar()
 
    Label(setup_window, text="Please setup your\nusername and password",bg="#000000", fg='#39ff14', width=35, height=4, font=("Lucida Bright", 20)).pack()
    Label(setup_window, text="",bg="#000000", fg='#39ff14').pack()
    username_lable = Label(setup_window, text="Username",bg="#000000", fg='#39ff14',font=("Ink Free", 20, "bold"))
    username_lable.pack()
    username_portal = Entry(setup_window, textvariable=username)
    username_portal.pack()
    password_lable = Label(setup_window, text="Password",bg="#000000", fg='#39ff14',font=("Ink Free", 20, "bold"))
    password_lable.pack()
    password_portal = Entry(setup_window, textvariable=password, show='*')
    password_portal.pack()
    Label(setup_window, text="",bg="#000000", fg='#39ff14').pack()
    Button(setup_window, text="Set-up",bd=5, width="20", height="1",bg="#000000", fg='#39ff14',font=("Lucida Bright", 20), command = setup_user).pack()



#Function for Login Window
 
def login():
    global login_window
    login_window = Toplevel(main_window)
    login_window['bg'] = '#000000'
    login_window.title("Login")
    login_window.geometry("600x400")
    Label(login_window, text="Please login through your\n Username and Password",bg="#000000", fg='#39ff14', width=40, height=4,font=("Lucida Bright", 20)).pack()
    Label(login_window, text="",bg="#000000", fg='#39ff14').pack()
 
    global username_validation
    global password_validation
 
    username_validation = StringVar()
    password_validation = StringVar()
 
    global username_login_portal
    global password_login_portal
 
    Label(login_window, text="Username",bg="#000000", fg='#39ff14',font=("Ink Free", 20, "bold")).pack()
    username_login_portal = Entry(login_window, textvariable=username_validation)
    username_login_portal.pack()
    Label(login_window, text="",bg="#000000", fg='#39ff14').pack()
    Label(login_window, text="Password",bg="#000000", fg='#39ff14',font=("Ink Free", 20, "bold")).pack()
    password_login_portal = Entry(login_window, textvariable=password_validation, show= '*')
    password_login_portal.pack()
    Label(login_window, text="",bg="#000000", fg='#39ff14').pack()
    Button(login_window, text="Login", width="20", height="1",bg="#000000", fg='#39ff14',font=("Lucida Bright", 20), command = login_validation).pack()

    
#Function for implementing event on setup button
 
def setup_user():
    username_info = username.get()
    password_info = password.get() 
    
    if len(str(password_info)) < 8:
        Label(setup_window, text="WARNING!\n Password should contain minimum 8 characters",bg="#000000", fg='#39ff14', width=45, height=4, font=("Lucida Bright", 10)).pack()
    else:
        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()
     
        username_portal.delete(0, END)
        password_portal.delete(0, END)
        Label(setup_window, text="Set-Up Success",bg="#000000", fg="#39ff14", font=("Ink Free", 20, "bold")).pack()

    
#Function for implementing event on login button
 
def login_validation():
    username1 = username_validation.get()
    password1 = password_validation.get()
    username_login_portal.delete(0, END)
    password_login_portal.delete(0, END)
 
    list_of_files = os.listdir()
    
    if username1 in list_of_files:
        
        file1 = open(username1, "r")
        validation = file1.read().splitlines()

        if password1 in validation:
            login_sucess()
                
        else:
            login_failure()
                
    else:
        user_not_found()


#Function for login Success Pop-up
 
def login_sucess():
    global login_success_window
    login_success_window = Toplevel(login_window)
    login_success_window['bg'] = '#000000'
    login_success_window.title("Success")
    login_success_window.geometry("600x400")
    Label(login_success_window, text="Login Successful",bg="#000000", fg='#39ff14', width="500", height="4", font=("Lucida Bright", 26)).pack()
    Button(login_success_window, text="OK",bg="#000000", fg='#39ff14', height="2", width="20",font=("Lucida Bright", 20), command=delete_login_success).pack()

    
#Function for login Failure Pop-up
 
def login_failure():
    global login_failure_window
    login_failure_window = Toplevel(login_window)
    login_failure_window['bg'] = '#000000'
    login_failure_window.title("Failure")
    login_failure_window.geometry("600x400")
    Label(login_failure_window, text="Login Failure\n (Password not recognized)",bg="#000000", fg='#39ff14', width="500", height="4", font=("Lucida Bright", 26)).pack()
    Button(login_failure_window, text="Try again !",bg="#000000", fg='#39ff14', height="2", width="20",font=("Lucida Bright", 20), command=delete_login_failure).pack()
    Button(login_failure_window, text="Reset",bg="#000000", fg='#39ff14', width="20", height="1",font=("Lucida Bright", 20), command = reset).pack()
                                  
    
#Function for reseting login information

def reset():
    setup()


#Function for User Not Found Pop-up
 
def user_not_found():
    global user_not_found_window
    user_not_found_window = Toplevel(login_window)
    user_not_found_window.title("User not Found")
    user_not_found_window.geometry("300x200")
    Label(user_not_found_window, text="User Not Found",bg="#000000", fg='#39ff14', width="500", height="3", font=("Lucida Bright", 26)).pack()
    Button(user_not_found_window, text="OK",bg="#000000", fg='#39ff14', height="2", width="20",font=("Lucida Bright", 20), command=delete_user_not_found_window).pack()


#Functions for deleting all Pop-ups
 
def delete_login_success():
    login_success_window.destroy()
 
 
def delete_login_failure():
    login_failure_window.destroy()
 
 
def delete_user_not_found_window():
    user_not_found_window.destroy()
 
 
#Function for Main Window
 
def main_account_window():
    global main_window
    main_window = Tk()
    main_window['bg'] = '#000000'
    main_window.geometry("650x570")
    main_window.title("Security System")
    Label(text="Choose your option", bg="#000000", fg='#39ff14', width="500", height="4", font=("Lucida Bright", 26)).pack()
    Label(text="",bg="#000000", fg='#39ff14').pack()
    Button(text="Login", height="4",bd=5, width="35",bg="#000000", fg='#39ff14',font=("Lucida Bright", 20), command = login).pack()
    Label(text="",bg="#000000", fg='#39ff14').pack()
    Button(text="Set-up", height="4",bd=5, width="35",bg="#000000", fg='#39ff14',font=("Lucida Bright", 20), command=setup).pack()
    
    main_window.mainloop()
 
 
main_account_window()
