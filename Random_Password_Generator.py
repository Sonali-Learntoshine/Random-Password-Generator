from tkinter import *
from tkinter import ttk
import random

scr = Tk(className="Random Password Generator")
scr.configure() #bg = 'brown')

label=Label(scr,text="Random Password Generator",bg="orange" ,font=("arial",25), borderwidth = 2, relief = "groove")
label.place(x = 200, y = 30)

def password_generator():
    len = num_slider.get()
    progress_bar['value'] = num_slider.get()
    if len <= 8:
        status_label.config(text = 'Weak')
    elif len <= 16:
        status_label.config(text = 'Strong')
    else:
        status_label.config(text = 'Excellent')
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '()[]{}*;/,._-'
    all = lower + upper + numbers + symbols
    password = ''.join(random.sample(all, len))
    show_pass.config(text = password)

def clear_scr(clear,clear1):
    clear['text'] = ''
    clear1['text'] = ''
    num_slider.set(6)
    progress_bar['value'] = 0


def choice():
    alpha, num, sym = 0,0,1

lb1 = Label(scr, text = "Password", font = ("arial", 10), width = 8)
lb1.place(x = 120, y = 160)

show_pass = Label(scr,bd = 10, width = 23, text = '', borderwidth = 2, relief = "sunken", bg = 'Lightgrey', font=("Calibri",25))
show_pass.place(x = 210, y=150)

lb2 = Label(scr, text = "Size Adjuster", font = ("arial", 10), width = 10)
lb2.place(x = 110, y = 215)

num_slider = Scale(scr, from_ = 1, to = 20, tickinterval = 1, orient = HORIZONTAL, length = 390, width = 10)
num_slider.set(6)
num_slider.place(x = 210, y = 200) 

lb3 = Label(scr, text = "Strength", font = ("arial", 10), width = 8)
lb3.place(x = 120, y = 255)

progress_bar = ttk.Progressbar(scr, orient = HORIZONTAL, length = 395, mode = 'determinate', maximum  = 20)
progress_bar.pack(pady = 20)
progress_bar.place(x = 210, y = 260)

status_label = Label(scr, font=("arial",10), width = 24)#, bg = 'white')
status_label.place(x = 210, y = 282)

button1 = Button(scr, text = 'Generate Password', command = password_generator, font=('arial',16), bg = 'lightgreen')
button1.place(x = 240, y = 330)

button2 = Button(scr, text = 'Reset', command = lambda : clear_scr(show_pass,status_label), font=('arial',16), bg = 'Lightblue')
button2.place(x = 490, y = 330)
 
scr.geometry("850x500")
scr.resizable(width = False, height = False)
scr.mainloop()

