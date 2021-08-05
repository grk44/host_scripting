
import pyinputplus as pyip
from datetime import datetime

response = pyip.inputNum('Enter num: ')
print(response)

r1 = pyip.inputMenu(['red','blue','green','orange'],prompt='Enter your favorite color:\n',numbered=True)
print(r1)


currentYear = datetime.now().year
currentMonth = datetime.now().month

date=pyip.inputDayOfMonth(currentYear,currentMonth,prompt='Enter a day of the month: ')
print(date)

state=pyip.inputUSState('Enter your State: ')
print(state)

state=pyip.inputUSState('Enter your State: ')
print(state)

ip=pyip.inputIP('Enter IP Address: ')
print(ip)

dir(pyip)


