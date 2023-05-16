#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

import numpy as np

def bubbleSort(a):
    passes = 0
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(a) - passes - 1):
            if (a[i] > a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
                sorted = False
        passes += 1
    return a
    

def insertionSort(a):
    for n in range(len(a) - 1):
        i = n + 1

        temp = a[i]
        while i > 0 and a[i-1] > temp:
            a[i] = a[i-1]
            i -= 1
        a[i] = temp
    return a

def selectionSort(array):
    for i in range(len(array)):
        minIdx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minIdx]:
                minIdx = j
        #swap
        array[i], array[minIdx] = array[minIdx], array[i]
    
    return array


def mergeSort(A):
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    mergeSortRecurse(A, 0, len(A) - 1)
    return A

def mergeSortRecurse(A, leftIdx, rightIdx):
    """ mergeSortRecurse - recursive merge sort algorithm
    """
    if leftIdx < rightIdx:
        midIdx = (leftIdx + rightIdx) // 2
        mergeSortRecurse(A, leftIdx, midIdx)
        mergeSortRecurse(A, midIdx + 1, rightIdx)
        merge(A, leftIdx, midIdx, rightIdx)

def merge(A, leftIdx, midIdx, rightIdx):
    """ merge - merge two sorted sub-arrays into one sorted array
    """
    tempA = np.zeros(rightIdx - leftIdx + 1)
    left = leftIdx
    right = midIdx + 1
    tempIdx = 0
    while left <= midIdx and right <= rightIdx:
        if A[left] < A[right]:
            tempA[tempIdx] = A[left]
            left += 1
        else:
            tempA[tempIdx] = A[right]
            right += 1
        tempIdx += 1
    while left <= midIdx:
        tempA[tempIdx] = A[left]
        left += 1
        tempIdx += 1
    while right <= rightIdx:
        tempA[tempIdx] = A[right]
        right += 1
        tempIdx += 1
    for i in range(len(tempA)):
        A[leftIdx + i] = tempA[i]
    return A

def quickSort(A): 
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    quickSortRecurse(A, 0, len(A) - 1)
    return A

def quickSortRecurse(A, leftIdx, rightIdx):
    """ quickSortRecurse - recursive quick sort algorithm
    """
    if leftIdx < rightIdx:
        pivotIdx = doPartitioning(A, leftIdx, rightIdx, leftIdx)
        quickSortRecurse(A, leftIdx, pivotIdx - 1)
        quickSortRecurse(A, pivotIdx + 1, rightIdx)

def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    """ doPartitioning - partition the array around the pivot
    """
    pivotVal = A[pivotIdx]
    A[pivotIdx], A[rightIdx] = A[rightIdx], A[pivotIdx]
    storeIdx = leftIdx
    for i in range(leftIdx, rightIdx):
        if A[i] < pivotVal:
            A[i], A[storeIdx] = A[storeIdx], A[i]
            storeIdx += 1
    A[storeIdx], A[rightIdx] = A[rightIdx], A[storeIdx]
    return storeIdx

if __name__ == "__main__":
    import random
    randomList = []
    for i in range(10):
        newNum = random.randint(0,10)
        randomList.append(newNum) 
    bubbleSort(randomList)