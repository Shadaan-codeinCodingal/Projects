file1 = open('inputfile.txt', 'r')
file2 = open('filepart2updated.txt','r')
file3 = open('mergefile.txt', 'w')
lines1 = file1.read()
lines2 = file2.read()
x = lines1 + "\n"+lines2
file3.write(x)
file1.close()
file2.close()
file3.close()
finalfile = open('mergefile.txt', 'r')
print("Reading the first file merged with the other one:")
print(finalfile.read())
finalfile.close()