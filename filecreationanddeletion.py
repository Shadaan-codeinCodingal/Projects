file1 =  open('filecreate1ert.txt','x')
file1.close()
print("file created")
import os
if os.path.exists('oddlines.txt'):
    os.remove('oddlines.txt')
    print('deleting oddlines.txt from memory')
else:
    print('oddlines.txt is not found and we could not delete it')