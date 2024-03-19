# -*- coding: utf-8 -*-
"""
Created on Wed May  3 07:45:59 2023

@author: USER
"""

from tkinter import *

root = Tk()
root.geometry("480x360")
root.title("Calculator")
root.configure(bg="#DDA429")

def addition():
    num1 = int(txt_num1.get())
    num2 = int(txt_num2.get())

    result = Label(root,bg = "#DDA429",width = 20,fg = "Black",text="The sum is: "+ str(num1+num2),font=20)
    result.place(x=160,y=210)

def subtraction():
    num1 = int(txt_num1.get())
    num2 = int(txt_num2.get())

    result = Label(root,bg = "#DDA429",width = 20,fg = "Black",text="The difference is: "+ str(num1-num2),font=20)
    result.place(x=160,y=210)

def multiplication():
    num1 = int(txt_num1.get())
    num2 = int(txt_num2.get())

    result = Label(root,bg = "#DDA429",width = 20,fg = "Black",text="The product is: "+ str(num1*num2),font=20)
    result.place(x=160,y=210)

def division():
    num1 = int(txt_num1.get())
    num2 = int(txt_num2.get())
    
    if num1 == 0:
        result = Label(root,bg = "#DDA429",width = 20,fg = "Black",text="Cannot be",font=20)
        result.place(x=160,y=210)
    elif num2 == 0:
        result = Label(root,bg = "#DDA429",width = 20,fg = "Black",text="Cannot be",font=20)
        result.place(x=160,y=210)
    else:
        result = Label(root,bg = "#DDA429",width = 20,fg = "Black",text=f"The quotient is: {num1/num2:.2f}",font=20)
        result.place(x=160,y=210)
    
def clear():
    txt_num1.delete(0,END)
    txt_num2.delete(0,END)
    result = Label(root,bg = "#DDA429",width=50)
    result.place(x=160,y=210)

header = Label(root,text="Submitted by: Ivan Emmanuel A. Dadacay",fg="Black",bg= "#DDA429",font=("Arial Black",12)).place(x=50,y=0)

lbl_num1 = Label(root,text="Num1",fg="Black",bg="#DDA429",font=("Arial Black",12)).place(x=140,y=50)
txt_num1 = Entry(root,width=15,border = 0)
txt_num1.place(x=120,y=90)

lbl_num2 = Label(root,text="Num2",fg="Black",bg="#DDA429",font=("Arial Black",12)).place(x=280,y=50)
txt_num2 = Entry(root,width=15,border = 0)
txt_num2.place(x=260,y=90)

btn_sum = Button(root,text="+",bg="#3B3837",width=4,border=0,font=12,command=addition).place(x=150,y=120)
btn_difference = Button(root,text="-",bg="#3B3837",width=4,border = 0,font=12,command=subtraction).place(x=200,y=120)
btn_product = Button(root,text="*",bg="#3B3837",width=4,border = 0,font=12,command=multiplication).place(x=250,y=120)
btn_quotient = Button(root,text="/",bg="#3B3837",width=4,border = 0,font=12,command=division).place(x=300,y=120)

btn_clear = Button(root,text="Clear",bg="#3B3837",width=21,border = 0,font=12,command=clear).place(x=148,y=155)

root.mainloop()