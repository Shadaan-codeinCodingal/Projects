file = open('Sample_file.txt', 'r')
print("Reading the file: ")
print(file.read())
file.close()
file = open('Sample_file.txt', 'w')
file.write("My name is Roy. I am in Class 8 and I am the class monitor.")
file.close()
file = open('Sample_file.txt', 'a')
file.write("\n MY favorite subject is Math.")
file.write("\nStudent --- Favorite Subject")
file.write("\nAlice --- Science")
file.write("\nBella --- English")
file.write("\nKaran --- 2nd Language")
file.write("\nMe --- Math")
file.write("\nArjun --- 3rd Language")
file.close()
file = open('Sample_file.txt')
print("Reading the file again.")
print(file.read())
file.close()