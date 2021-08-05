import re
plants=open("plants.xml","r")
pcsv=open("plants.csv","w+")



plantname = re.compile(r'<COMMON>(.*)</COMMON>')
price = re.compile(r'<PRICE>(.*)</PRICE>')

for plant in plants:
    p=plantname.search(plant)
    try:
        print(p.group(1)+'\t',end =" ")
        pcsv.write(p.group(1)+';')
    except:
        pass
    d = price.search(plant)
    try:
        print(d.group(1))
        pcsv.write(d.group(1)+'\n')
    except:
        pass

plants.close()
pcsv.close()
