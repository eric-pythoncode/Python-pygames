from tkinter import *

screen = Tk()
screen.title("Speed Calculator")

def bttn_average():
    hour = float(txt_hour.get())
    min = float(txt_min.get())
    dist = float(txt_dist.get())
    average = dist / (hour + (min / 60))
    lbl_averagespeed.config(text=f"{average:.2f} Km/hr")

lbl_title = Label(win, text="Average Speed Calculator", width = 40, font=("Times New Roman", 20), fg = "green", borderwidth=2, relief="solid")

lbl_hour = Label(win, text="Hours", width = 20, font=("Times New Roman", 12, "bold"), fg = "green", relief="solid")
lbl_min = Label(win, text="Minutes", width = 20, font=("Times New Roman", 12, "bold"), fg = "green", relief="solid")
lbl_dist = Label(win, text="Distance (KM)", width = 20, font=("Times New Roman", 12, "bold"), fg = "green", relief="solid")


bttnaverage = tkm.Button(screen, text="Average", width=150, height = 40,fg="lightblue",bg="black", font=("Times New Roman", 20, "bold"), borderwidth=2, relief="solid", command=bttn_average)

lbl_averagespeed = Label(win, text="", width = 50, borderwidth = 2, font=("Times New Roman", 12, "bold"), fg = "green", relief="solid")

lbl_title.grid(row=0, column=0, columnspan=2, padx=10)
lbl_hour.grid(row=1, column=0, columnspan=2, pady=20)
lbl_min.grid(row=2, column=0, columnspan=2, pady=20)
lbl_dis.grid(row=3, column=0, columnspan=2, pady=20)
txt_hour.grid(row=1, column=1, columnspan=2)
txt_min.grid(row=2, column=1, columnspan=2)
lbl_dis.grid(row=3, column=1, columnspan=2)
bttn_average.grid(row=4, column=0, columnspan=2)
lbl_averagespeed.grid(row=5, column=0, columnspan=2, pady=20)




mainloop()