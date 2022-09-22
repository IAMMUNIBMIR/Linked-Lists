mylinkedList =  [27, 19, 36, 42, 16, None, None, None, None, None, None, None]
myLinkedListPointers = [-1, 0, 1, 2, 3 ,6 ,7 ,8 ,9 ,10 ,11, -1]
startPointer = -1
heapStartPointer = 0
index = 0

itemSearch = 0
itemPointer = 0
nullPointer = -1


for index in range(len(mylinkedList)):

    if mylinkedList[index] == None:
        startPointer = index - 1
        break
    
    else:
        index += 1
    

def find(itemSearch):

    found = False
    itemPointer = startPointer

    while itemPointer != nullPointer and not found:

        if mylinkedList[itemPointer] == itemSearch:
            found = True

        else:
            itemPointer = myLinkedListPointers[itemPointer]
            
    return itemPointer



def insert(itemAdd):
    
    global startPointer,heapStartPointer
    
    if heapStartPointer == nullPointer:
        print("Linked List full")
        
    else:
        tempPointer = startPointer
        startPointer = heapStartPointer
        heapStartPointer = myLinkedListPointers[heapStartPointer]
        mylinkedList[startPointer] = itemAdd
        myLinkedListPointers[startPointer] = tempPointer



def delete(itemDelete):
    
    global startPointer, heapStartPointer
    
    if startPointer == nullPointer:
        print("Linked List empty")
    
    else:
        index = startPointer
        oldindex = 0

        while mylinkedList[index] != itemDelete and index != nullPointer:
        
            oldindex = index
            index = myLinkedListPointers[index]
        
        if index == nullPointer:
            print("Item ", itemDelete, " not found")

        else:
            mylinkedList[index] = None
            tempPointer = myLinkedListPointers[index]
            myLinkedListPointers[index] = heapStartPointer
            heapStartPointer = index
            myLinkedListPointers[oldindex] = tempPointer



item = int(input("Please enter item to be found "))
result = find(item)

if result != -1:
    print("Item found")
    
else:
    print("Item not found")


