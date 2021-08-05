import re
phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
mo = phoneNumRegex.search('My number is 415-555-4242.  My other phone is 123-456-6789.')
print('Phone number found: ' + mo.group())
print ("1:" + mo.group(1))
print ("2:" + mo.group(2))
print ("3:" + mo.group(3))

print ("\nFindall\n")
phone2=re.compile(r'(\d{3})-(\d{3})-(\d{4})')
x=phone2.findall('My office number is 814-362-7666.  Wes\'s cell number is 555-123-4567')
print(x)
print(x[0])
print(x[1])
print(x[0][0])