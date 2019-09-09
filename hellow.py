from tkinter import *  # 1-- basic window open
root = Tk() # 1-- basic window open
# root.minsize(300,300) # minimum size of the window
root.geometry("400x400") # adjustable window
root.resizable(0,0) # window size is fixed now

un = Entry(root,font=("Arial",20),fg = "blue")
un.pack()


root.mainloop()  # 1-- basic window open
