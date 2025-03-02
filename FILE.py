with open('Sample_File.txt','w') as l:
    l.write('My name is Shadaan.')
l.close()
with open('Sample_File.txt','r') as x:
    x.readlines()
    for i in x:
        y = i.split()
        print(y)
x.close()
import os
if os.path.exists('My_File.txt'):
    print('My_File.txt exists')
else:
    print('My_File.txt does not exists')
    x = open('My_File.txt','x')
    x.close()
    x = open('My_File.txt','w')
    x.write('My name is Shadaan')
    x.close()
    print('Creating file My_File.txt')
    print('...')
    print('My_File.txt exists')
    x.close()
if os.path.exists('My_File.txt'):
    print('Deleting My_File.txt')
    print('....')
    os.remove('My_File.txt')
    print('My_File.txt has been deleted')
else:
    print('Could not delete My_File.txt')