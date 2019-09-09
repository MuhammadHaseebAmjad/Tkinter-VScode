from tkinter import *  # 1-- basic window open
root = Tk() # 1-- basic window open
# root.minsize(300,300) # minimum size of the window
root.geometry("400x400") # adjustable window
root.resizable(0,0) # window size is fixed now
un = Label(root,text = "SoftWare") # print label of the window
un.pack() # label is not printed without pack
un2 = Label(root, text = "Softwear size change", font = ("Arial",15))
un2.pack()
root.mainloop()  # 1-- basic window open
# print("jaan")