import re,logging as log

# DEBUG,INFO,WARNING,CRITICAL
#log.basicConfig(level=log.INFO, format=' %(asctime)s -%(levelname)s -  %(message)s')
#log.basicConfig(filename='myProgramLog.txt', level=log.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
def Error1(y):
   raise Exception("That is not a number!")
   #log.debug("That is not a number!: "+y)

x=input('Enter radius: ')
#the line below will produce a stack trace if the value entered is not a float
#assert float(x)

check=re.search(r'\d+\.?\d*',str(x))

if check:
    area=3.14*float(x)**2
    print('Area is',area)

else:
    Error1(x)




