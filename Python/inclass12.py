import re

file = open("libs.txt","r")

mlib = re.compile(r'ADJECTIVE|NOUN|VERB')
madlib=""
for line in file:
	lib=mlib.findall(line)
	print(lib)
	n=0
	for x in lib:		
		#repl=input("Enter {0}:".format(x))
		repl='TEST'+str([n])
		line = re.sub(lib[n],repl,line,1)
		#print(line)
		n=n+1
	#print(line)

	madlib= madlib+line
print(madlib)

# 	for q in repl:
# 		madlib = re.sub(lib,repl,line)
# 		print(madlib)

	#madlib = re.sub(mlib, TO SEARCH,# of times to replace)
	#re.sub(thing to find, replace with, what to use on, occurances to do)
	#print(lib)