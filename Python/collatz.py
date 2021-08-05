
def collatz(number):
	if number % 2 == 0:
	    num=number//2
	    print(num)
	    return num

	elif number % 2 == 1:
	    num=3*number+1
	    print(num)
	    return num


number = int(input("Enter a number:"))

while number > 1:
    number = collatz(number)
