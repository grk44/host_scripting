import pyinputplus as pyip

ans= pyinputplus.inputYesNo

#======================
import pyinputplus as pyip

response = pyip.inputYesNo("Would you like to know how to keep an idiot busy for hours? ")
print(response)

while response == 'yes':
    response = pyip.inputYesNo("Would you like to know how to keep and idiot busy for hours? ")


#+============
import pyinputplus as pyip

x=1
while True:
    y=pyip.inputYesNo( prompt='Would you like to know how to keep an idiot busy for hours?:\n')
    print(y)
    if y=='no':
        break