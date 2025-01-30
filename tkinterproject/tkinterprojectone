import tkinter as tk
from tkinter import messagebox

screen = tk.Tk()
screen.title("Log in screen")
screen.config(bg="#FFF")
screen.geometry("400x300")

#function
def logincheck():
    uname = "me"
    password = "12345"
    if entry.get() == uname and passcodeinput.get() == password:
        messagebox.showinfo(title="Login" , message = "Login successful")
    else:
        messagebox.showerror(title="Failed, check password or username")

#design
title = tk.Label(screen, text = "Login" , bg = "yellow" , fg = "black" , font = ("Times New Roman", 20 , "bold"))
title.grid(row = 0, column = 0)

name = tk.Label(screen, text = "Username" , bg = "yellow" , fg = "black" , font = ("Times New Roman", 20 , "bold"))
name.grid(row = 1, column = 0)

entry = tk.Entry(screen, text = "" , bg = "yellow" , fg = "black" , font = ("Times New Roman", 20 , "bold"))
entry.grid(row = 1, column = 1)

passcode = tk.Label(screen, text = "Password" , bg = "yellow" , fg = "black" , font = ("Times New Roman", 20 , "bold"))
passcode.grid(row = 2, column = 0, padx = 10, pady = 10)

passcodeinput = tk.Entry(screen, text = "" , bg = "yellow" , fg = "black" , font = ("Times New Roman", 20 , "bold"))
passcodeinput.grid(row = 2, column = 1, padx = 10, pady = 10)

login = tk.Button(screen, text = "LOGIN" , bg = "yellow" , fg = "black" , font = ("Times New Roman", 20 , "bold"), command = logincheck)
login.grid(row = 3, column = 0, padx = 10, pady = 10, columnspan = 2)
screen.mainloop()