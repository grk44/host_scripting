import re,csv
plants=open("plants.xml","r")
pcsv=open("plants2.csv","w")
csvwriter=csv.writer(pcsv,delimiter='|',lineterminator='\n')




plantname = re.compile(r'<COMMON>(.*)</COMMON>')
price = re.compile(r'<PRICE>(.*)</PRICE>')
plantlist = []
for plant in plants:
    p=plantname.search(plant)

    try:
        plantlist.append(p.group(1))
        #print(p.group(1)+'\t',end =" ")
    except:
        pass
    d = price.search(plant)
    try:
        plantlist.append(d.group(1))
        #print(d.group(1))
        #pcsv.write(d.group(1)+'\n')
        print(plantlist)
        csvwriter.writerow(plantlist)
        plantlist = []
    except:
        pass

plants.close()
pcsv.close()
