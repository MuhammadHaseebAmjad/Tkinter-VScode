from tkinter import *  # 1-- basic window open
root = Tk() # 1-- basic window open
# root.minsize(300,300) # minimum size of the window
root.geometry("400x400") # adjustable window
root.resizable(0,0) # window size is fixed now

l1 = Label(root,text = "Enter Name",font = ("Arial",15))
l1.grid(row = 0,column = 0,pady = 25,sticky = W) #pady for give space

e1 = Entry(root, font = ("Arial",15))
e1.grid(row = 0,column = 1,pady = 25) #pady for give space

l2 = Label(root,text = "Enter Password",font = ("Arial",20))
l2.grid(row = 1,column = 0,pady = 25) #pady for give space

e2 = Entry(root, font = ("Arial",15))
e2.grid(row = 1,column = 1,pady = 25) #pady for give space

b1 = Button(root,text = "Login",font=("Arial",15))
b1.grid(row = 2,column =0,columnspan = 2)

root.mainloop()  # 1-- basic window open
