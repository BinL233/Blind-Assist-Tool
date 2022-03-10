from tkinter import *
root = Tk()
root.geometry('600x300')
root.title("Blind Assist Tool")


bg = PhotoImage(file = "background.png")
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)
label2 = Label(root, text = "Welcome", bg = "#FCC3A5",fg = "#3D5D72")
label2.pack(pady = 50)

frame1 = Frame(root)
frame1.pack(pady = 20 )

