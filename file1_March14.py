#create a program thate lets the user knowis the file exist, and the user can write into it. it should ask if the user wants to write into it. and let the user write
file = input('Enter name of file: ')
try :
    openfile = open(file, 'a')
    print('File exist')
except:
    print('File does not exist')
    quit()
openfile = open(file, 'a')
ans = input('would you like to write to the file? (y/n): ')
if ans.lower() == "y" :
    #openfile = open('file', 'a')
    #wrt_file = openfile.write('come over ')
    #print(wrt_file)
    openfile.write('\nThere comes a time when we heard')
    print(openfile)
    openfile.close()
else:
    print('Cannot write to file')
