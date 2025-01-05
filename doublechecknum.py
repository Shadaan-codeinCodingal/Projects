number = int(input("Enter the number: "))

if number > 50:
    print("Number is greater than 50.")
    if number % 2 == 1:
        print("The number is odd.")
    else:
        print("The number is even.")
else:
    print("The number is less than 50.")