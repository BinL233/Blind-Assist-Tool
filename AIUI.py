from tkinter import *
import os
import tkinter.font as font

root = Tk()
root.geometry('600x300')
root.resizable(False,False)
root.title("Blind Assist Tool")

path1 = os.path.abspath(__file__)
path = os.path.dirname(path1)

canvas = Canvas(width=600, height=300, highlightthickness=0, borderwidth=0)
canvas.place(x=0, y=0)
Imagepath = str(path) + '\\Images\\background_600.png'

bg = PhotoImage(file=Imagepath)
bgid = canvas.create_image(0, 0, image=bg, anchor='nw')

ft = font.Font(family = 'Microsoft yahei', size = 15, weight=font.BOLD)
label2 = Label(root, text = "Welcome", bg = "#FCC3A5",fg = "#3D5D72", font = ft)
label2.pack(pady = 50)

frame1 = Frame(root)
frame1.pack(pady = 20 )

root.mainloop()

