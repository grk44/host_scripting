#Load the OS module
import os


#retrieve the user profile directory
homedir=os.environ['HOME']

for root, dirs, files in os.walk(homedir):
   print(root)
   # print(dirs)
   #   print(files)


#test to see if a path exists
os.path.exists(homedir+'/.bashrc')

#specify directory to check
newdir = homedir + '/mynewdir'
#test if dir exits
os.path.exists(newdir)
#create directory if it does not exist
os.path.exists(newdir) or os.mkdir(newdir)
#check to see if it was created
os.path.exists(newdir)
#remove the directory
os.rmdir(newdir)
#check to see if it exists now
os.path.exists(newdir)

#run a system command
os.system('ls -l ' + homedir) #produces directory listing of homedirectory
os.system('ls -l ' + homedir) # passes a command to the system