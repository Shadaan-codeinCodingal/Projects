from tkinter import *
from PIL import Image, ImageTk
window = Tk()
window.title('TkInter Image of UK Flage')
window.geometry('2000x2000')
uploadflag = Image.open('27119.jpg')
flag = ImageTk.PhotoImage(uploadflag)
label1 = Label(window, image=flag, width=500, height = 700)
label1.place(x=50, y=50)
label2 = Label(window, text = 'UK Flag', bg = 'red', fg='green', width = 200)
label2.place(x=50, y=100)
window.mainloop()