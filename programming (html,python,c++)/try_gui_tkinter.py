from tkinter import *

root = Tk()

root.geometry("700x300")
root.title("Calculator ni Avah")

frame1 = LabelFrame(text="Label sample")
frame1.pack()
lbl_1 = Label(frame1, 
              bg = "magenta",
              fg= "white",
             
              font = ("Lucida Handwriting", 10, "italic"), 
              height= 5, 
              padx = 50, #indicates the spaces horizontally
              pady = 50, #vertically
              text = "owo",)
lbl_1.pack()

frame2 = LabelFrame(text="message sample ")
frame2.pack()
msg_1 = Message(frame2,
                
                text = "Hi Welcome!")
msg_1.pack()

root.mainloop()