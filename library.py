class Library:
    def __init__(self, books, name):
        self.bookList = books
        self.name =name
        self.lendDict={}
    def display(self):
        print("Welcome to the {} Library. We have the following books.".format(self.name))
        for book in self.bookList:
            print(book)
    def lendBook(self, bookname, username):
        if bookname not in self.bookList:
            print("Sorry! We do not have that book.")
        elif bookname in self.lendDict:
            print("Sorry! That book is already taken by", self.lendDict[bookname])
        else:
           self.lendDict[bookname] = username
           print("We have this book. You can take it.")
           self.bookList.remove(bookname)
    def addBook(self, bookadd):
        self.bookList.append(bookadd)
        print("This book has been added to the Library Collection! Thank you for your contribution of {}.".format(bookadd))
objectuser = Library(["Python", "Rich Dad Poor Dad", "Harry Potter", "Charlie and the Chocolate Factory", "Math Mind"], "Let's Upskill")
user_name = input("What is your name? ")
while True:
    print(f"Hello {user_name}! Welcome to the Library {objectuser.name} Choose an option 1, 2, 3.")
    print("1. Display a Book 2. Lend A book 3. Add a book")
    userchoice = input("Choose an option. ")
    if userchoice not in ["1", "2", "3"]:
        print("Please select a valid option")
        continue
    elif userchoice == "1":
        objectuser.display()
    elif userchoice == "2":
        bookchoose = input("Which book are you choosing? ")
        objectuser.lendBook(bookchoose, user_name)
    elif userchoice == "3":
        bookchoose = input("What book do you want to add? ")
        objectuser.addBook(bookchoose)
    else:
        break