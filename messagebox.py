from tkinter import *
from tkinter import messagebox
window = Tk()
window.title('Virus Scanner')
window.geometry('500x500')
def scanvirus():
    messagebox.showwarning('Alert', 'Virus Found')
button = Button(window, text = 'Scan Virus', command = scanvirus)
button.pack()
window.mainloop()