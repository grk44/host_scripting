import re

def datecheck(data):
	detectdate=re.compile(r'(\d{0,2}\/\d{1,2}\/\d{4})(?:\s|\,)')
	founddates=detectdate.findall(data)
	for i in founddates:
		print('Date Found: {0}'.format(i))
		datesplit=i.split("/")		
		month = int(datesplit[0])
		day = int(datesplit[1])
		year = int(datesplit[2])
		print('Is Valid = {0}'.format(validcheck(month, day, year)))

def validcheck(month, day, year):
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


stuff="some string or text with dates, real like 10/3/1999 or 5/18/2022, fake or bad dates like 00/33/200, 13/8/20034, and 04/31/2021 <- april only has 30 days"
print(datecheck(stuff))
