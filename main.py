test = [2, 4, 6, 8, 10, 1, 5]    
test1 = [2, 5, 10, 20, 21]

def contains(aList, item):
    for el in aList:
        if el == item:
            return True
    return False

def indexOf(aList, item):
    for x in range(0, aList):
        if(aList[x] == item):
            return x
    return "-1"

def reverse(aList):
    reversed = []
    for x in range(len(aList)-1, -1, -1):
        reversed.append(aList[x])
    return reversed

def swap(aList, index1, index2):
    first_Val = 0 
    second_Val = 0
    first_Val = aList[index1]
    second_Val = aList[index2]
    aList[index1] = second_Val
    aList[index2] = first_Val

def indexOfMin(aList):
    min  = aList[0]
    y = 0
    for x in range(0, len(aList)):
        if(aList[x] < min):
            y = x
    return x


##### Not allowed to use Index
print(indexOf(test, 5))