#using graph, hash table, heap

import Dependancies.DSAGraph as DSAGraph
import Dependancies.DSAhash as DSAhash
import Dependancies.DSAHeap as DSAHeap
import Dependancies.DSALinkedList as DSALinkedList
import numpy as np
import DSAUav

def ezFlightParse(linkedList:DSALinkedList.DSALinkedList):
    #turns linked list into array
    arrayLen = len(linkedList)
    array = np.empty(arrayLen, dtype=object)
    idx = 0
    for vert, weight in iter(linkedList):
        array[idx] = vert.getLabel()
        idx += 1
    return array

def main():
    uav = DSAUav.UAV()
    uav.importFile("txtFiles/location.txt", "txtFiles/UAVdata.txt")

    print("------[Adjacency List]------")
    uav.display()
    print("------[Flight test]---------")

    #testing flight paths
    start = "A"
    end = "J"
    print(f"Flight path from {start} to {end}:")
    flightPath, distance = uav.travel(start, end)
    path = ezFlightParse(flightPath)
    print("Flight path: ", path)
    print("Distance: ", distance)

    print("------[parseToTable]--------")
    #parsing flight path to hash table
    table = uav.pathToTable(flightPath)
    for item in table.displayTable():
        if item.getValue() is not None:
            #skip empty indexes
            print(item.getKey(), item.getValue())

        



if __name__ == "__main__":
    main()