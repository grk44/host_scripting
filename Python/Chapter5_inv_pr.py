#Display inventory project
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(k,v)
        item_total = item_total + v
    print("Total number of items: " + str(item_total))

print("=== Fantasy Game Inventory Project===")
displayInventory(stuff)

#add to inventory project
def addToInventory(inventory, addedItems):
    # your code goes here
    #iterate through the items to be added
	for x in addedItems:
		#if the item to be added has a key already, add 1 to the value
		if x in inventory.keys():
			#print(inventory[x])
			inventory[x] = inventory[x]+1
		#if no existing key found, make one and add value of 1
		else:			
			inventory[x] = 1
			#print(inventory[x], 'added')
	return inventory    

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
print("\n=== List to Dictionary Function for Fantasy Game Inventory Project===")
displayInventory(inv)