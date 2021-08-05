import re

data="some string or text with dates, real like 10/3/1999 or 5/18/2022, fake or bad dates like 00/33/200, 13/8/20034, and 04/31/2021 <- april only has 30 days"
detectdate=re.compile(r'(\d{0,2}\/\d{1,2}\/\d{4})(?:\s|\,)')

class datestore:
	def __init__(self, month, day, year):
		self.month = month
		self.day = day
		self.year = year


#for i in data:
founddates=detectdate.findall(data)
print('Found Dates')
print(founddates)

for i in founddates:
	datesplit=i.split("/")
	print('Split Done')
	print(datesplit)
	month = datesplit[0]
	day = datesplit[1]
	year = datesplit[2]

	#is month valid?
	if month > 0 and month < 13:
		return True		
		#is month Feb?
		if month == 2:
			return True			
			#leapyear check
			if year % 4 == 0:
				#is a leap year?
				if year % 100 != 0 or year % 400 == 0:									
					if day > 0 and day < 30:
						return True
					else:
						return False
				elif day > 0 and day < 29:
					return True
				else:
					return False
			#not a leap year, Feb has 28 days
			elif day > 0 and day < 29:
				return True
			else:
				return False
		#check for Apr, Jun, Sep, Nov
		elif month == 4 or month == 6 or month == 9 or month == 11:
			if day > 0 and day < 31:
				return True
			else:
				return False
		#any other month
		else:
			if day > 0 and day < 32:
				return True
			else:
				return False






	#leapyear check
	# if year % 4 == 0:
	# 	if year % 100 != 0:


	# print('month = {0}'.format(month))
	# print('day = {0}'.format(day))
	#store=datestore(datesplit)
	#print(store)
	# for o in datesplit:
	# 	print(o)

# x = datestore('test1', 'test2', 'test3')
# print(x.month)

# y = ['test1', 'test2', 'test3']
# print(y)
# y1=tuple(y)
# y2=str(y1)
# print(y1)
# print(y2)



# z= datestore(y1)
# print(y1.month)

# class datestore:
# 	def __init__(self, month, day, year):
# 		self.month = month
# 		self.day = day
# 		self.year = year
