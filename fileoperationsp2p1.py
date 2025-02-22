with open('filep3.txt', 'w') as file:
    file.write("Hi! I am penguin and I am 9 years old.")
file.close()
with open('filep3.txt', 'r') as file:
    x = file.readlines()
    for i in x:
        y = i.split()
        print(y)
file.close()