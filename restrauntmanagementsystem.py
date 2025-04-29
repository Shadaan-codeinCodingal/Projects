import tkinter as tk
from tkinter import ttk
class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class MyOrder:
    def __init__(self):
        self.foods = []
    def add(self, food, qty):
        self.foods.append((food, qty))
    def total(self):
        return sum(f.price * q for f, q in self.foods)
    def bill_text(self):
        lines = ["    Delicious Diner    ", " 123 Foodie Lane, Yumtown",
                 "GSTIN: 27AABCU9603R1Z2", "-------------------------------",
                 "{:<12}{:<5}{:<8}{}".format("Item", "Qty", "Rate", "Total"),
                 "-------------------------------"]
        for f, q in self.foods:
            lines.append("{:<12}{:<5}{:<8}{}".format(f.name, q, f.price, f.price * q))
        lines.append("-------------------------------")
        lines.append(f"Total Bill: Rs {self.total()}")
        lines.append("Thank you for dining with us!")
        lines.append("Visit Again :)")
        return "\n".join(lines)
class RestaurantGame:
    def __init__(self, win):
        self.win = win
        win.title("Delicious Diner POS")
        self.foods = [Food("Pizza", 120), Food("Burger", 80),Food("Pasta", 100), Food("Salad", 70),Food("Fries", 50), Food("Coke", 30),Food("Ice Cream", 60), Food("Brownie", 90),Food("Soup", 75), Food("Garlic Bread", 40)]
        self.order = MyOrder()
        self.setup()
    def setup(self):
        self.tree = ttk.Treeview(self.win,
                               columns=("Name", "Price", "Qty", "Total"),
                               show='headings')
        self.tree.heading("Name", text="Item")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Qty", text="Qty")
        self.tree.heading("Total", text="Total")
        self.tree.grid(row=0, column=0, columnspan=4)
        self.food_name = tk.StringVar()
        self.food_menu = ttk.Combobox(self.win, textvariable=self.food_name,
                                     values=[f.name for f in self.foods],
                                     state="readonly")
        self.food_menu.grid(row=1, column=0)
        self.qty = tk.IntVar(value=1)
        ttk.Entry(self.win, textvariable=self.qty, width=5).grid(row=1, column=2)
        ttk.Button(self.win, text="Add", command=self.add).grid(row=1, column=3)
        ttk.Button(self.win, text="Bill", command=self.bill).grid(row=2, column=3)
        self.bill_box = tk.Text(self.win, height=12, width=40)
        self.bill_box.grid(row=3, column=0, columnspan=4)
    def add(self):
        food_name = self.food_name.get()
        qty = self.qty.get()
        if food_name and qty > 0:
            for food in self.foods:
                if food.name == food_name:
                    self.order.add(food, qty)
                    self.tree.insert('', 'end',
                                    values=(food.name, food.price, qty,
                                            food.price * qty))
                    break
    def bill(self):
        self.bill_box.delete("1.0", tk.END)
        self.bill_box.insert(tk.END, self.order.bill_text())
win = tk.Tk()
app = RestaurantGame(win)
win.mainloop()