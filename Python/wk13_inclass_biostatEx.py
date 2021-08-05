import csv

csvop = open('biostats.csv')
csvread = csv.reader(csvop)
#print(csvread)

for x in csvread:
	for q in x:
		r=q.strip()
		print(r)
		global csvstrip
		csvstrip = ""
		csvstrip=csvstrip+"{0},".format(r)
	
	print(csvstrip)
		


# for x in csvread:
# 	print(x)
#     #print("Name: " + x["Name"] +"\nSex: " +x["Sex"])
# csvfile.close()


# for x in csvread:
# 	print(x)