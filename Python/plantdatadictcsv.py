# import the regex and csv modules
import re,csv
#open file to parse
plants=open("plants.xml","r")
#open file to write to
pcsv=open("plants3.csv","w+")
#initialize the CSV dictionary writer with colun names Plant and Price and a pipe delimter
csvwriter=csv.DictWriter(pcsv,['Plant','Price'],delimiter='|')
#write the header to the file
csvwriter.writeheader()

#setup our regex
plantname = re.compile(r'<COMMON>(.*)</COMMON>')
price = re.compile(r'<PRICE>(.*)</PRICE>')
#initialize dictionary
plantlist = {}

for plant in plants:
    p=plantname.search(plant)
    #test to seed if search finds anything
    if plantname.search(plant):
        #if there is a match set the PLANT key equal to the value of group 1 from the regex search
        plantlist['Plant']=p.group(1)
    d = price.search(plant)
    # test to see if second search finds anything
    if price.search(plant):
        #if there is a match set the PRICE key equal tot he value of group 1 from the second regex search
        plantlist['Price']=d.group(1)
        #print dictionary to the screen
        print(plantlist)
        #write dictionary to the csv file
        csvwriter.writerow(plantlist)
        #reinitialize dictionary
        plantlist = {}


#close files
plants.close()
pcsv.close()
