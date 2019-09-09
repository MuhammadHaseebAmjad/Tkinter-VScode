from tkinter import *  # 1-- basic window open
root = Tk() # 1-- basic window open
# root.minsize(300,300) # minimum size of the window
root.geometry("400x400") # adjustable window
root.resizable(0,0) # window size is fixed now

l1 = Label(root,text = "Enter Name",font = ("Arial",20))
l1.grid(row = 0,column = 0,pady = 25)

e1 = Entry(root, font = ("Arial",20))
e1.grid(row = 0,column = 1,pady = 25)

root.mainloop()  # 1-- basic window open
