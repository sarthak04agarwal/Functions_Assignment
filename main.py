test = [2, 4, 6, 8, 10]    
test1 = [2, 5, 10, 20, 21]

def contains(aList, item):
    if item in test1:
        return( str(item) + " is IN the list")
    else:
        return( str(item) + " is NOT in the list")


'''
while(running):
    for x in range(0, len(test)):
        if (item == aList[x]):
            running = False
            print( str(item) + " is IN the list")
    else:
        print( str(item) + " is NOT in the list")
'''

list_name = input("Please enter the name of the list that you want to check: ")
item_List = input("Please enter the item that you want to search inside the list: ")
print(contains(list_name, item_List))