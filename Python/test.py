#print(ord("@"))
#print(chr(99))

#Mystring = "PythonIsProgrammingLanguage"

#print('Original String :', Mystring)

#print('Splitting String By Position :',
     # [Mystring[i:i+1] for i in range(0, len(Mystring), 1)])
#splitline=[Mystring[i:i+1] for i in range(0, len(Mystring), 1)]
#print('split by single character', splitline)


#file_name = input('Enter file name if in this folder or full path\n.txt file name:')
# file_name = open("test.txt")
# chars=[]
# for x in file_name:	
# 	#chars.append([x[i:i+1] for i in range(0, len(x), 1)])
# 	chars.append(x)
# 	#print(chars)


# #print(chars)
# nums=[]
# for y in chars:
# 	#print(y)
# 	for q in y:		
# 		nums.append(ord(q))
# 		#print(q)


# newf = open("unicoded.txt","w")
# newf.close()
# for z in nums:
# 	f=open("unicoded.txt","a")
# 	s=str(z)
# 	f.write(s+'$@$@')
# 	f.close()

# var1 = 8
# tvar = 4
# var2 =var1 % tvar
# var3 =var1 / tvar
# print(var2,'\n',var3)

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * self.length + 2 * self.width

# # Here we declare that the Square class inherits from the Rectangle class
# class Square(Rectangle):
#     def __init__(self, length):
#         super().__init__(length, length)

# square = Square(4)
# print(square.area())

# from collatz import *
# number = 5
# collatz(number)


# print('Hello, world!'[3:])
    # 
    # 'Hello, world!'[:5]
    # 'Hello, world!'[3:]
    

# print('Remember, remember, the fifth of November.'.split())
# print('-'.join('There can be only one.'.split()))
# >>> spam = '    Hello, World    '
# >>> spam.strip()
# 'Hello, World'
# >>> spam.lstrip()
# 'Hello, World    '
# >>> spam.rstrip()
# '    Hello, World'

# import re

# string = 'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected. The ADJECTIVE ADJECTIVE NOUN VERB over the ADJECTIVE NOUN.'




# def adjectives(string):
    
#     Ads = re.search('(ADJECTIVE)', str(string))
#     i=0
#     while True:
#         try:
#             match = Ads.group(i)
#             print(match)
#         except:
#             break
#         if match == None:
#             break
#         else:
#             ans = input('Enter an adjective: ')
#             madlib = re.sub("(ADJECTIVE)", str(ans), string, 1)
#             string = madlib
#             i+=1
#     return string


# def verbs(string):
#     verbs = re.search('(VERB)', string)  
#     i=0
#     while True:
#         try:
#             match = verbs.group(i)
#             print(match)
#         except:
#             break
#         if match == None:
#             break
#         else:
#             ans = input('Enter an adjective: ')
#             madlib = re.sub("(VERB)", str(ans), string, 1)
#             string = madlib
#             i+=1
#     return string
# def verbs(string):
#     verbs = re.search('(VERB)', string)  
#     i=0
#     while True:
#         try:
#             match = verbs.group(i)
#             print(match)
#         except:
#             break
#         if match == None:
#             break
#         else:
#             ans = input('Enter an adjective: ')
#             madlib = re.sub("(VERB)", str(ans), string, 1)
#             string = madlib
#             i+=1
#     re
# def verbs(string):
#     verbs = re.search('(VERB)', string)  
#     i=0
#     while True:
#         try:
#             match = verbs.group(i)
#             print(match)
#         except:
#             break
#         if match == None:
#             break
#         else:
#             ans = input('Enter an adjective: ')
#             madlib = re.sub("(VERB)", str(ans), string, 1)
#             string = madlib
#             i+=1
#     return string


# def nouns(string):
#     nouns = re.search('(NOUN)', string)
#     i=0
#     while True:
        
#         try:
#             match = nouns.group(i)
#             print(match)
#         except:
#             break
#         if match == None:
#             break
#         else:
#             ans = input('Enter an adjective: ')
#             madlib = re.sub("(NOUN)", str(ans), string, 1)
#             string = madlib
#             i+=1
#     return string



# string = adjectives(string)
# string = nouns(string)
# string = verbs(string)
# print(string)

# bread='White'
# prot = 'tofu'
# total=float(0.00)
# if bread == 'Sourdough':
#     print(bread, '$1.99')
#     total = total + 1.99
# if bread != 'Sourdough':
# 	print(bread, '$0.99')
#     total=total+0.99
# if prot == 'Chicken' or prot == 'Turkey':
#     print(prot, '$0.99'

# import os
# test=os.path('C:/Users')/'A1'
# print(test)



print("hello There!!!")