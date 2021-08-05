import csv
csvfile = open('users.csv')
csvreader = csv.reader(csvfile)
#csvdata = list(csvreader)
#print(csvdata)

for row in csvreader:
    if csvreader.line_num >1:
        print("Username: " + row[0]+ "\nPassword: " + row[2])

# DictReader

import csv
csvfile = open('users.csv')
csvdictreader = csv.DictReader(csvfile)
for user in csvdictreader:
    print("Username: " + user['Username'] +"\nPassword: " +user['One-time password'])
csvfile.close()

#writing csvs
import csv
mycsvfile = open('mycsvfile.csv','w',newline='')
csvWriter = csv.writer(mycsvfile,delimiter=';',lineterminator='\n')
csvWriter.writerow(['process','cputime','mem(k)'])
csvWriter.writerow(['grep','1:05','32'])
csvWriter.writerow(['vi','2:34','128'])
mycsvfile.close()

#using dict writer
import csv
mydictcsvfile = open('mycsvfile2.csv','w',newline='')
csvwriter=csv.DictWriter(mydictcsvfile,['process','cputime','mem(k)'],delimiter='|')
csvwriter.writeheader()
csvwriter.writerow({'process':'grep','cputime':'1:05','mem(k)':'32'})
csvwriter.writerow({'process':'vi','cputime':'2:34','mem(k)':'128'})
mydictcsvfile.close()