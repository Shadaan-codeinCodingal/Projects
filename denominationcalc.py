from tkinter import *
from tkinter import messagebox
w1 = Tk()
w1.title('Denomination Calculator')
w1.configure(bg='blue')
w1.geometry('600x450')
label = Label(w1, text='Welcome to the Denomination Calculator Application', bg='red')
label.pack()
def msg():
    navigator1 = messagebox.showinfo('Alert', 'Do you want to calculate?')
    if navigator1 == 'ok':
        topwin()
button = Button(w1, text='Go to Denomination Calculator', command=msg, bg='red', fg='yellow')
button.pack()
def topwin():
    top = Toplevel()
    top.title('Demoination Calculator Interface')
    top.geometry('600x450')
    top.configure(bg='blue')
    lbl =Label(top, text='Enter the amount', bg='red')
    lbl.pack()
    entry = Entry(top)
    entry.pack()
    lbl1 = Label(top, text='The denominations are listed below', bg = 'grey')
    lbl1.pack()
    l1 = Label(top, text='Denomination of 1000', bg = 'lightgrey')
    l1.pack()
    e1 = Entry(top)
    e1.pack()
    l2 = Label(top, text='Denomination of 500', bg = 'lightgrey')
    l2.pack()
    e2 = Entry(top)
    e2.pack()
    l3 = Label(top, text='Denomination of 200', bg = 'lightgrey')
    l3.pack()
    e3 = Entry(top)
    e3.pack()
    def calculate():
        try:
            global amount
            amount = int(entry.get())
            note1000 = amount // 1000
            amount = amount%1000
            note500 = amount//500
            amount = amount%500
            note200 = amount//200
            amount = amount%200
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e1.insert(END, str(note1000))
            e2.insert(END, str(note500))
            e3.insert(END, str(note200))
        except ValueError:
            messagebox.showerror('Error','Please enter a valid number that can be calculated(multiples of 100).')
    buttoncalculate = Button(top, text='Calculate denominations', bg = 'light grey', command=calculate)
    buttoncalculate.pack()
    top.mainloop()
w1.mainloop()