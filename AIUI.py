from tkinter import *
root = Tk()

VoiceOver = Button(root, text = "voice over", padx = 20, pady = 20, fg = 'black')
VoiceOver.pack()
root.geometry('600x300')
VoiceOver.place(x = 20, y = 50)

Checkout = Button(root, text = "Checkout", padx = 20, pady = 20, fg = 'black')
Checkout.pack()
root.geometry('600x300')
Checkout.place(x =240, y = 50)

Help = Button(root, text = "More Info", padx = 20, pady = 20, fg = 'black')
Help.pack()
root.geometry('600x300')
Help.place(x = 450, y = 50)

root.title("Blind Assist Tool")
root.mainloop()

