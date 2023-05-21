import numpy as np

def prime(n):
    nextPrime = int(n + 1)
    prime = True
    while True:
        for i in range(2, nextPrime):
            if nextPrime%i ==0:
                prime = False
                break
        if prime:
            return int(nextPrime)
        else:
            nextPrime = nextPrime + 1
            if nextPrime % 2 == 0:
                nextPrime = nextPrime + 1
            prime = True
            return int(nextPrime)

class DSAHashEntry:

    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.state = 0 #0 is empty 1 is filled -1 formerly used

    def getKey(self): return self.key
    def getValue(self): return self.value
    def getState(self): return self.state
    def setKey(self, key): self.key = key
    def setValue(self, value): self.value = value
    def setState(self, state): self.state = state

class DSAHashTable:


    def __init__(self, size = None):
        if size is None:
            size = 100
        self.hashArray = np.empty(prime(size), dtype = "object")
        self.loadFactor = None
        self.size = prime(size)
        self.MAX_LOAD = 0.99
        self.MIN_LOAD = 0.3
        self.MAX_STEP = 3
        for i in range(prime(size)):
            self.hashArray[i] = DSAHashEntry()
        
    def hashFunction(self, key, bound = None):
        #modified to accept strings
        key = ord(key)
        if bound is None:
            bound = self.size
        hashIndex = (key << 5) + (key << 2) + key
        '''old:
        for _ in range(len(str(key))):
            hashIndex += hashIndex ^ ((hashIndex << 5) + (hashIndex << 2) + int(str(key)[_]))
        '''
        return abs(hashIndex % bound)

    def stepHash(self, key):
        hashStep = 1 + self.hashFunction(key) % self.size
        return abs(hashStep % self.size)

    def put(self, key, value):
        found = False
        giveUp = False
        hashIdx = self.hashFunction(key)
        originalIdx = hashIdx
        loadFactor = self.getLoadFactor()
        if loadFactor >= self.MAX_LOAD:
            size = prime(int(self.size * 1.5))
            self.resize(size)
            self.size = size

        while not found and not giveUp:
            if self.hashArray[hashIdx].getState() == 0 or self.hashArray[hashIdx].getState() == -1:
                found = True
                self.hashArray[hashIdx].setKey(key)
                self.hashArray[hashIdx].setValue(value)
                self.hashArray[hashIdx].setState(1)

            elif self.hashArray[hashIdx].getKey() == key:
                found = True
                self.hashArray[hashIdx].setValue(value)

            else:
                hashIdx += self.stepHash(key)
                hashIdx = hashIdx % self.size

                if hashIdx == originalIdx:
                    giveUp = True

        if not found:
            raise NodeExistError("Error: hash table is full")
    
        return hashIdx

        
    def get(self, key):
        found = False
        giveUp = False
        hashIdx = self.hashFunction(key)
        originalIdx = hashIdx

        while not found and not giveUp:
            if self.hashArray[hashIdx].getState() == 0:
                giveUp = True

            elif self.hashArray[hashIdx].getKey() == key:
                found = True

            else:
                hashIdx += self.stepHash(key)
                hashIdx = hashIdx % self.size

                if (hashIdx == originalIdx):
                    giveUp = True

        if not found:
            raise NodeExistError("Error: key does not exist")
        
        return self.hashArray[hashIdx].getValue()

    def remove(self, key):
        found = False
        giveUp = False
        hashIdx = self.hashFunction(key)
        originalIdx = hashIdx

        while not found and not giveUp:
            if self.hashArray[hashIdx].getState() == 0:
                giveUp = True
            
            elif self.hashArray[hashIdx].getKey() == key:
                found = True
                replacement = DSAHashEntry()
                self.hashArray[hashIdx] = replacement
                self.hashArray[hashIdx].setState(-1)
            
            else:
                hashIdx += self.stepHash(key)
                hashIdx = hashIdx % self.size

                if hashIdx == originalIdx:
                    giveUp = True

        if self.getLoadFactor() <= self.MIN_LOAD:
            size = prime(self.size/2)
            self.resize(int(size))
            self.size = size
            
    def getLoadFactor(self):
        numItems = 0
        for i in self.hashArray:
            if i.getState() == 1:
                numItems += 1
        return ( numItems / self.size )
    
    def resize(self, size):
        temp = DSAHashTable(size)
        for i in self.hashArray:
            if i.getState() == 1:
                temp.put(i.getKey(), i.getValue())
        self.hashArray = temp.hashArray
        self.size = temp.size

    def importCSV(self, file):
        '''
        import a csv and put into hashArray
        '''
        with open(file + '.csv', 'r') as f:
            data = f.read().split('\n')
            for i in data:
                temp = i.split(',')
                print("hashing " + temp[1])
                self.put(int(temp[0]), temp[1])

    def exportArray(self, file):
        '''
        export hashArray into csv file
        '''
        with open(file + '.csv', 'w') as f:
            for i in self.hashArray:
                if i.getState() == 1:
                    f.write(str(i.getKey()) + ',' + str(i.getValue()) + '\n')

    def displayTable(self):
        return self.hashArray

class NodeExistError(Exception):
    pass
