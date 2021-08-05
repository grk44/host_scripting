import pyinputplus as pyip

bread=pyip.inputMenu(['Wheat','White','Sourdough'],prompt='Select a Bread:\n',numbered=True)
prot=pyip.inputMenu(['Chicken','Turkey','Ham','Tofu'],prompt='Select a Protein:\n',numbered=True)

cheeseYN=pyip.inputYesNo('Would you like cheese?')
if cheeseYN == 'yes':
    cheese=pyip.inputMenu(['Cheddar','Swiss','Mozzarella'],prompt='Select a Cheese:\n',numbered=True)
else:
    cheese='No Cheese'

condYN=pyip.inputYesNo('Would you like mayo, mustard, lettuce, or tomato?')
cond='Add - '
if condYN == 'yes':
    mayo=pyip.inputYesNo('Add mayo?')
    if mayo == 'yes':
        cond = 'mayo '
    mustard=pyip.inputYesNo('Add mustard?')
    if mustard == 'yes':
        cond = cond + 'mustard '
    lettuce=pyip.inputYesNo('Add lettuce?')
    if lettuce == 'yes':
        cond = cond + 'lettuce '
    tomato=pyip.inputYesNo('Add tomato?')
    if tomato == 'yes':
        cond = cond + 'tomato'
else:
    cond = cond + 'None'

count=pyip.inputInt('How many Sandwiches to order?: ', min=1)

#Recipt

total=float(0.00)
if bread == 'Sourdough':
    print(bread, '$1.99')
    total = total + 1.99
if bread != 'Sourdough':
    print(bread, '$0.99')
    total = total + 0.99
if prot == 'Chicken' or prot == 'Turkey':
    print(prot, '$0.99')
    total = total + 0.99
if prot == 'Ham' or prot == 'Tofu':
    print(prot, '$1.25')
    total = total + 1.35
print(cheese, '$0.50')
total = total + 0.50
print(cond)
print('Number of Sandwich: ',count)
total = total * count
print('Total: ${0}'.format(total))