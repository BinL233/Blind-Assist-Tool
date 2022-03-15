import tkinter as tk
import time
import sys

class Display(tk.Frame):
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


if __name__ == '__main__':
    Display().mainloop()