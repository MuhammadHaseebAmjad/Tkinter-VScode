from tkinter import *  # 1-- basic window open
root = Tk() # 1-- basic window open
# root.minsize(300,300) # minimum size of the window
root.geometry("400x400") # adjustable window
root.resizable(0,0) # window size is fixed now

b1 =Button(root,text = "Click !!!",font = ("Arial",20),fg = "green") 
b1.pack()


root.mainloop()  # 1-- basic window open
