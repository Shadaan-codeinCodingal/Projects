inputfile = open('inputfile.txt', 'r')
outputfile = open('uniquelines.txt', 'w')
lines = set()
for line in inputfile:
    if line not in lines:
        outputfile.write(line)
        lines.add(line)
print("All unigue lines in inputfile.txt are:")
print(lines)
inputfile.close()
outputfile.close()