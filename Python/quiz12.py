numOK=0
while numOK != 1:	
	num = int(input("Type a number between 1 and 10:"))
	if num >0 and num <11:
		numOK=1
	else:
		print('Bad Value, Try Again\n')		

if num > 5:
	numx = num * 10
	x=0
	while x > numx:		
		print(x)

elif num < 5:
	numx = num * 5	
	for r in range(numx):
		print(r)

elif num == 5:
	num5 = num

print('The result is {0}'.format(numx))