#read (r), write (w) append (a) 

try :
    filehandle = open('demo.txt', 'a')
    print(filehandle)
except filenotfound: 
    print('file does not exist')
else:
    print('file successfully created/opened')


try :
    filehandle = open('demo.txt', 'r')
    print(filehandle.read())
except filenotfounderror: 
    print('file does not exist')
except unsupportedOperation:
    print('yo can read the rile')
else:
    print('file successfully created/opened')


from io import UnsupportedOperation
try :
    filehandle = open('demo.txt', 'a')
    print(filehandle.read())
    filehandle.close()
except FileNotFoundError: 
    print('file does not exist')
except UnsupportedOperation:
    print('you can read the file')
    ans = input('would you still like to read the file? (y/n): ')
    if ans.lower() == "y" :
        filehandle = open('demo.txt', 'a')
        print(filehandle.read())
        filehandle.close()
else:
    print('file successfully created/opened')


f = open('demo.txt', 'r')
print(f.read(5))
print(f.readline())

#you can also perform a for loop
for x in f:
    print(x)

#close file
f.close()

# write content into a file
f = open('demo.txt', 'a')
f.write('Now the file has more content!')
f.close()
#open and read the file after the appending
f = open('demo.txt', 'r')
print(f.read())

#create a program thate lets the user knowis the file exist, and the user can write into it. it should ask if the user wants to write into it. and let the user write

