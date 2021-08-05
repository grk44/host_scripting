import random

numberOfStreaks = 0

for experimentNumber in range(10000):
	flips = []
    #creates array/list of 100 flips, 0 or 1
	for x in range(100):
		rnum = random.randint(0,1)
		flips.append(rnum)
	#sets counts of streak to 0
	headcount = 0
	tailcount = 0
	#iterates through the array/list of 0 and 1
	for y in flips:
		ht = flips[y]
		#if the flip is "heads" 1 
		if ht == 1:
			headcount = headcount+1
			if headcount == 6:
				numberOfStreaks = numberOfStreaks + 1
				headcount = 0
			tailcount = 0
		elif ht == 0:
			tailcount = tailcount+1
			if tailcount == 6:
				numberOfStreaks = numberOfStreaks + 1
				tailcount = 0
			headcount = 0    	

    

print('Chance of streak: %s%%' % (numberOfStreaks / 100))




