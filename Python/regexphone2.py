import re

phone = re.compile(r'(\d{3})-(\d{3})-(\d{4})') # prepare a regex statement.  use r'' treats as raw string. no escape
p = phone.search('My office number is 814-362-7666')
print(p.group(0)) #print the matched string
print(p.group(1) + " is the area code") # print the first group
print(p.group(2) + " is the prefix") # print the 2nd group
print(p.group(3) + " is the line number") # print the 3rd group
print("All groups are: " + str(p.groups())) # print all groups

phone2=re.compile(r'(\d{3})-(\d{3})-(\d{4})')
x=phone2.findall('My office number is 814-362-7666.  Wes\'s cell number is 555-123-4567')
print(x)

