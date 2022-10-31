test = [2, 4, 6, 8, 10]    

def contains(aList, item):
    running = True

while(running):
    for x in range(0, len(test)):
        if (item == aList[x]):
            running = False
            print( str(item) + " is IN the list")
    else:
        print( str(item) + " is NOT in the list")
    

aList = input("Please enter the name of the list: ")
item = input("Please enter the item that you want to search inside the list: ")

contains()