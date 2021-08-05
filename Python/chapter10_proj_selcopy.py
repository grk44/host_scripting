import os, shutil

# findext=input("What extention would you like to find?\nEnter like '.txt':")
# findloc=input('\nWhere would you like to search?\nEnter Absolute or relative path:')
# cpto=input('\nWhere would you like to copy the files to?\nEnter Absolute or Relative path:')

findext=".txt"
findloc="./testfile"
cpto="./testfile/test2"

x=os.scandir(findloc)
for i in x:
	#print('\n{0}'.format(i))
	for q in i:
		print(q)

		if len(findext) == 4:
			if i[-4:] == findext:
				#print(findloc,i,cpto)
				#shutil.copy(findloc / i, cpto / i)
				pass
		if len(findext) == 3:
			if i[-3:] == findext:
				#print(findloc,i,cpto)
				#shutil.copy(findloc / i, cpto / i)
				pass
