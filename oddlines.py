file = open('filepart2.txt', 'r')
file2 = open('oddlines.txt', 'a')
lines=file.readlines()
for i in range(1, len(lines)+ 1):
    if (i % 2) ==0:
        pass
    else:
        file2.write(lines[i-1])
print("Reading the entire file:")
for line in lines:
    print(line)
file.close()
file2.close()
file2 =open('oddlines.txt', 'r')
print("Reading only odd lines of the file:")
print(file2.read())
file2.close()