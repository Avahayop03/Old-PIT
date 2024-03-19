from tkinter import *

root = Tk()
root.title("Main Window")
root.geometry("1920x1080")

pic = PhotoImage(file = "daisy.jpg" )
canvas = Canvas(root, width=1920, height = 1080)
canvas.pack(side=LEFT)
canvas.create_image(0,0,image=pic,anchor="nw")
root.mainloop()