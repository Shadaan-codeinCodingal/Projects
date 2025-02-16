file = open('filepart2.txt', 'r')
file2 = open('filepart2updated.txt', 'a')
for line in file.readlines():
    if not(line.startswith('I')):
        print("Adding this line to file 2:")
        print(line)
        file2.write(line)
file.close()
file2.close()
file2 = open('filepart2updated.txt', 'r')
print("Reading file 2:")
print(file2.read())
file2.close