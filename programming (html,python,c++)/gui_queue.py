from tkinter import *
from queue import Queue

q_window = Tk()
queue= Queue()
q_window.title("Queue Window")
q_window.geometry("600x310")
q_window.resizable(False,False)
q_window.config(bg="#D6D831")
frame = Frame(width= 200, height=100,bg="white")
frame.place(x=200, y=160)

entry = Entry(width=20)
entry.place(x=240,y=50)
label = Label(text="Queue is empty", bg="white")
label.place(x=255,y=200)
label1= Label(q_window, text="Results:", bg= "white", font=("Documan",12, "bold"),)
label1.place(x=270, y=160)
def enqueue():
    item = entry.get()
    if item:
        queue.put(item)
        label.config(text=f"Queue: {list(queue.queue)}",bg="white")
        entry.delete(0, END)
        label.place(x=210,y=200)

def dequeue():
    if not queue.empty():
        item = queue.get()
        label.config(text=f"Queue: {list(queue.queue)}", bg="white")
        entry.delete(0, END)
        
    else:
        label.config(text=f"Queue: {list(queue.queue)}    Queue is empty!", bg="white")
        entry.delete(0, END)

def clear_queue():
    queue.queue.clear()
    label.config(text=f"Queue is empty", bg="white")   


#buttons
eq= Button(q_window, font= ("Berlin Sans FB Demi", 12,"bold"), text="Enqueue", border=0, cursor="hand2", width =15, command=enqueue, bg="white")
eq.place(x=230, y=80)
dq= Button(q_window, font=("Times", 12, "bold"), text="Dequeue", border=0, cursor="hand2", width =15, command=dequeue, bg="white")
dq.place(x=230, y=125)
cq = Button(q_window, font=("Times", 12, "bold"), text="Clear Queue", border=0, cursor="hand2", width=15,command=clear_queue, bg="white")
cq.place(x=230, y=265)


        
q_window.mainloop()
