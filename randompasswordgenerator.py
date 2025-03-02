from tkinter import *
import random
window = Tk()
window.title("Random Password Generator")
window.geometry("500x500")
def Generate_password():
    letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password = ""
    for i in range(10):
        l = random.randint(1,3)
        if l == 1:
            password += random.choice(letters)
        elif l == 2:
            password += random.choice(numbers)
        else:
            password += random.choice(symbols)
    password_label.config(text=f"Generated Password: {password}")

password_label = Label(window, text="Generated Password: ")
password_label.pack(pady=20)

button = Button(text="Generate Password", command=Generate_password, bg="blue", fg="white")
button.pack(pady=10)

window.mainloop()