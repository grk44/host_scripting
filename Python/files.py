import os

print(os.getcwd())


newdir='MyTestDir' # variable to store new directory
usr=os.environ['USER'] # retrieve usernname from bash variable
print(usr) # print out username
d=os.path.join('/','home',usr,'Documents') # setup path
print(d) # output path


os.chdir(d) # change directories
print(os.getcwd()) # print current directory

md = os.path.join(d,newdir)
if not os.path.exists(md):
        os.makedirs(md)
print('1. Dir listing is: ' + str(os.listdir(md)))

hw = os.path.join(md,'hw.txt')

file = open(hw, 'w')
file.write('Hello World!\n')
file.close()
file=open(hw,'a')
file.write('Bacon is not a vegetable')
file.close()

print('2. Dir listing is: ' + str(os.listdir(md)))

file=open(hw)
content=file.read()
file.close()
print('3. File content is: ' + str(content))
