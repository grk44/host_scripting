import re
import os

userin=input('Enter a regular expression to search for:\n')

regc=re.compile(userin)
files=os.scandir(path='.')
for i in files:
    if i.name.endswith('.txt') and i.is_file():
        fname=str(i.name)
        #print(fname)
        file=open(fname)
        print(i.name)
        for z in file:
            regex= regc.findall(z)
            if regex != []:
                print(regex)
            else:
                pass