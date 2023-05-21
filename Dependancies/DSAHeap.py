import numpy as np

class DSAHeapEntry():
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value
    
    def __str__(self):
        return (self.priority, self.value)
    
    def getPriority(self):
        return self.priority
    def getValue(self):
        return self.value
    def setPriority(self, priority):
        self.priority = priority
    def setValue(self, value):
        self.value = value

class DSAHeap():
    def __init__(self, size):
        self.heap = np.empty(size, dtype=object)
        self.count = 0

    def __str__(self):
        return str(self.heap[:self.count])

    def __len__(self):
        return self.count
    
    def isEmpty(self):
        return self.count == 0
    
    def isFull(self):
        return self.count == len(self.heap)
    
    def insert(self, priority, value):
        if self.isFull():
            raise IndexError("Heap is full")
        else:
            self.heap[self.count] = DSAHeapEntry(priority, value)
            self.count += 1
            self.trickleUp(self.count - 1)

    def trickleUp(self, index):
        parentIndex = (index - 1) // 2
        if index > 0 and self.heap[index].getPriority() < self.heap[parentIndex].getPriority():
            self.swap(index, parentIndex)
            self.trickleUp(parentIndex)

    def swap(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp

    def remove(self):
        if self.isEmpty():
            raise IndexError("Heap is empty")
        else:
            value = self.heap[0].getValue()
            prio = self.heap[0].getPriority()
            self.count -= 1
            self.heap[0] = self.heap[self.count]
            self.trickleDown(0)

            self.heap[self.count] = None #item actually gets removed from array

            return prio, value
        
    def trickleDown(self, index):
        leftIndex = index * 2 + 1
        rightIndex = index * 2 + 2
        if leftIndex < self.count:
            if rightIndex < self.count:
                if self.heap[leftIndex].getPriority() < self.heap[rightIndex].getPriority():
                    minIndex = leftIndex
                else:
                    minIndex = rightIndex
            else:
                minIndex = leftIndex
            if self.heap[minIndex].getPriority() < self.heap[index].getPriority():
                self.swap(minIndex, index)
                self.trickleDown(minIndex)
    
    def peek(self):
        if self.isEmpty():
            raise FullHeapError("Error, full heap")
        else:
            return self.heap[0].getValue()

    def export(self):
        '''
        exports heap to array
        '''
        array = np.empty(self.count, dtype=object)
        for i in range(self.count):
            array[i] = self.remove()
        return array

    def display(self):
        if self.isEmpty():
            raise EmptyHeapError("Error, empty heap")
        else:
            for i in self.heap:
                if i is not None:
                    print(f"priority: {i.getPriority()} | value: {i.getValue()}")

    def __len__(self):
        return self.count

class EmptyHeapError(Exception):
    pass

class FullHeapError(Exception):
    pass

class ExistingItemError(Exception):
    pass