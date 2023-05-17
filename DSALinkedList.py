'''
linkedLists with head/tail attributes

slightly modified for prac6, allowing deletion of nodes at any point in the list
'''

class DSAListNode:

    def __init__(self,value):
        self.value = value
        self.nextNode = None
        self.previousNode = None

    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value

    def getNext(self):
        return self.nextNode

    def setNext(self,value):
        self.nextNode = value

    def getPrev(self):
        return self.previousNode

    def setPrev(self,value):
        self.previousNode = value

    #iterator using pseudocode // changed some values to work with code
    def __iter__(self):
        self.cursor = self.head
        return self
    
    def __next__(self):
        cursorValue = None
        if self.cursor is None:
            raise StopIteration
        else:
            cursorValue = self.cursor.getValue()
            self.cursor = self.cursor.getNext()
        return cursorValue

    def __prev__(self):
        cursorValue = None
        if self.cursor is None:
            raise StopIteration
        else:
            cursorValue = self.cursor.getValue()
            self.cursor = self.cursor.getPrev()
        return cursorValue

class DSALinkedList(DSAListNode):

    def __init__(self):
        self.head = None #object in the leftmost side
        self.tail = None #object in the rightmost side
        self.ndCount = 0


    def isEmpty(self):
        if self.head is None and self.tail is None:
            return True
        else:
            return False

    def insertFirst(self,value): #insert a new value in the left side, head
        self.ndCount += 1
        newNode = DSAListNode(value)
        if self.isEmpty() is True:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.setNext(self.head) #self.head is the same as self._root in page 69
            self.head = newNode
        return newNode

    def insertLast(self,value): #insert a new value in the right side, tail
        self.ndCount += 1
        newNode = DSAListNode(value)
        if self.isEmpty() is True:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.setNext(newNode)
            newNode.setPrev(self.tail)
            self.tail = newNode
        return newNode

    def peekFirst(self):
        if self.isEmpty() is True:
            return None
        else:
            return self.head.getValue()
        
    def peekLast(self):
        if self.isEmpty() is True:
            return None
        else:
            return self.tail.getValue()

    def removeFirst(self):
    
        if self.isEmpty() is True:
            retVal = None
        if self.ndCount == 0:
            raise ValueError() #empty linkedList
        if self.ndCount == 1:
            retVal = self.head.getValue()
            self.head = None
            self.tail = None
        else:
            retVal = self.head.getValue()
            self.head = self.head.getNext()
            self.head.setPrev(None)
        self.ndCount -= 1
        return retVal

    def removeLast(self):

        if self.isEmpty() is True:
            return None

        if self.ndCount == 1:
            retVal = self.tail.getValue()
            self.head = None
            self.tail = None

        else:
            retVal = self.tail.getValue() #value to be deleted 
            self.tail = self.tail.getPrev()
            self.tail.setNext(None)

        self.ndCount -= 1
        return retVal
#-------------------------------------------------

    def isIn(self, item):
        node = self.head
        while node.getNext() is not None:
            if node.getValue() == item:
                return True
            else:
                node = node.getNext()
        return False

    def __len__(self):
        return self.ndCount
    
    def removeItem(self, item): #removes node regardless of position
        ...

#-------------------------------------------------
        
class ListError(Exception):
    pass


if __name__ == "__main__":
    ll = DSALinkedList()
    for i in list(range(1,10)):
        ll.insertLast(i)
    
    print(ll.removeFirst())

    print(ll.head.getValue())
    print(ll.tail.getValue())

    print("_-----------------_")
    for value in iter(ll):
        print(value)