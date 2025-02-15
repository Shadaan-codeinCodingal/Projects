file = open('file.txt', 'r')
count = 0
lines = file.read()
x = lines.split("\n")
for i in x:
    if i:
        count += 1
print("The number of lines in this file is ")
print(count)
file.close()