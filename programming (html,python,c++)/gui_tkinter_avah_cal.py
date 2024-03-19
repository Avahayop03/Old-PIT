from tkinter import *

root = Tk()

root.title("Calculator ni Avahkeks")
root.geometry("500x200")


def prod():
    num1 = int(txt1_num.get())
    num2 = int(txt2_num.get())

    result = Label(root,fg = "Black",width = 20, text="product: " + str(num1*num2),font=20)
    result.place(x=125,y=100)
    
def sub():
    num1 = int(txt1_num.get())
    num2 = int(txt2_num.get())

    result = Label(root,fg = "Black",width = 20,text="difference: "+ str(num1-num2),font=20)
    result.place(x=125,y= 100)
    
def divid(): 
    num1 = int(txt1_num.get())
    num2 = int(txt2_num.get())
    if num1 == 0:
        result = Label(root, fg= "Red", width= 30, text="Any number divided by 0 is 0.",font=20)
        result.place(x=125,y=100)
    elif num2 == 0:
        result = Label(root,fg="Red", width= 30, text="Note: Division by 0 is undefined!", font=20)
        result.place(x=125,y=100)
    else:
        result = Label(root,fg = "Black",width = 40,text="qoutient: "+ str(num1/num2),font=20)
        result.place(x=125,y=100)
    
def add():
    num1 = int(txt1_num.get())
    num2 = int(txt2_num.get())

    result = Label(root,fg = "Black",width = 20,text="sum: "+ str(num1+num2),font=20)
    result.place(x=125,y=100)
    

def clear():
    txt1_num.delete(0,END)
    txt2_num.delete(0,END)
    result = Label(root,width=50)
    result.place(x=125,y=100)


    
    
#
num1 = Label(root, text= "first number: ")
txt1_num = Entry(root) 
num2= Label(root, text= "second number: ")
txt2_num = Entry(root) 




#operations btns/labels 
btn_multi = Button(root, text= "[*] Multiplication",bg="gray", fg="white", relief= RAISED,width=15,padx= 10, command=prod,cursor="hand2")
btn_sub = Button(root, text= "[-] Subtraction",bg="gray", fg="white", relief= RAISED,width=15,padx= 10, command=sub,cursor="hand2")
btn_divid = Button(root, text= "[/] Division",bg="gray", fg="white",  relief= RAISED,width=15,padx= 10, command=divid,cursor="hand2")
btn_add = Button(root, text= " [+] Addition", bg="gray", fg="white",   relief= RAISED,width=15,padx= 10, command=add,cursor="hand2")
btn_clear = Button(root, text= "Clear All",bg="gray", fg="white", relief= RAISED,padx = 10, command = clear,cursor="hand2")
L_res = Label(root, text = "Results... ",fg = "red", height= 2, font = ("Arial", 10, "italic"),cursor="wait")

#geometry manager_1
num1.grid(row = 0 , column = 0)
txt1_num.grid(row = 0 , column = 1)
num2.grid(row = 0 , column = 2)
txt2_num.grid(row = 0 , column = 3)


#operations
btn_multi.grid(row = 2, column = 1) #columnspan/rowspan means duha ka columns/rows occupied
btn_sub.grid(row = 2, column =2)
btn_divid.grid(row = 3, column = 1)
btn_add.grid(row = 3, column = 2)
btn_clear.grid(row=2, column = 3, rowspan = 2)
L_res.grid(row = 4, column =0, columnspan=4)



root.mainloop()