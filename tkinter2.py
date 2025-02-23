from tkinter import *
window = Tk()
window.configure(bg='red')
window.title('Table')
window.geometry("206x206")
for i in range(3):
    for j in range(3):
        frame = Frame(master=window, bg='white',relief=RAISED, borderwidth=1)
        frame.grid(row=i, column=j,padx=3,pady=3)
        label = Label(master=frame, text=f'Row{i+1}, \n Column{j+1}')
        label.pack()
window.mainloop()