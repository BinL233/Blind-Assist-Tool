from tkinter import *
import os
import tkinter
import tkinter.font as font
import main
import message

'''
class Display(tkinter.Frame):
    def __init__(self):
       tk.Frame.__init__(self)
       self.doIt = tk.Button(self,text="Start", command=self.start, background = 'black', fg='white')
       self.doIt.pack()

       self.output = tk.Text(self, width=100, height=15, background = 'black', fg='white')
       self.output.pack(side=tk.LEFT)

       self.scrollbar = tk.Scrollbar(self, orient="vertical", command = self.output.yview)
       self.scrollbar.pack(side=tk.RIGHT, fill="y")

       self.output['yscrollcommand'] = self.scrollbar.set

       self.count = 1
       self.configure(background='black')
       self.pack()


    def start(self):
        if self.count < 1000:
            self.write(str(self.count) + '\n')
            print (self.count)
            self.count += 1
            self.after(2000, self.start)


    def write(self, txt):
        self.output.insert(tk.END,str(txt))
        self.update_idletasks()
'''

def start():
    x = main.start()
    write(x)

def func(event):
    start()

def write(txt):
    output.insert(tkinter.END,str(txt))
    root.update_idletasks()

root = Tk()
root.geometry('600x320')
root.resizable(False, False)
root.title("Blind Assist Tool")

path1 = os.path.abspath(__file__)
path = os.path.dirname(path1)

canvas = Canvas(width=600, height=320, highlightthickness=0, borderwidth=0)
canvas.place(x=0, y=0)
Imagepath = str(path) + '/Images/background_600.png'

bg = PhotoImage(file=Imagepath)
bgid = canvas.create_image(0, 0, image=bg, anchor='nw')

ft = font.Font(family='Microsoft yahei', size=15, weight=font.BOLD)
label2 = Label(root, text="Welcome", bg="#FCC3A5", fg="#3D5D72", font=ft)
label2.pack(pady=50)

frame1 = Frame(root)
frame1.pack(pady=20)

output = tkinter.Text(width=100, height=15, background = 'black', fg='white')
output.place(x=110, y=135, width=380, height=140)

scrollbar = Scrollbar(orient="vertical", command = output.yview)
scrollbar.place(x=110, y=135, width=380, height=140)

output['yscrollcommand'] = scrollbar.set




AIUIS = message.AIUI()
AIUIS.start()

root.bind("<Key>",func)




#ft2 = font.Font(family='Microsoft yahei', size=17)
#button1 = Button(root, text='Voice Over',
                 #bg='#F7DFDF', command=start, font=ft2)
#button1.place(x=110, y=135, width=380, height=140)


root.mainloop()
