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

def threatTracker(uav:DSAUav.UAV, start:str):
    '''
    DFS and store in heap depending on the threat level
    '''
    #thresholds
    '''
    temp:
        25-32 = 1
        33-40 = 2
        >40 = 3
        
    humidity:
        >50 = 1
        31-50 = 2
        <30 = 3
        
    wind speed:
        <40 = 1
        41-55 = 2
        >55 = 3
    
    level of threat is determined by adding all values together
    '''
    dataHeap = DSAHeap.DSAHeap(uav.locationCount)
    path, distance = uav.DFS(start)
    for vert, weight in iter(path):
        temp = int(vert.getValue().getTemperature())
        humidity = int(vert.getValue().getHumidity())
        windSpeed = int(vert.getValue().getWindSpeed())
        threatLevel = 0
        if temp >= 25 and temp <= 32:
            threatLevel += 3
        elif temp >= 33 and temp <= 40:
            threatLevel += 2
        elif temp > 40:
            threatLevel += 1

        if humidity > 50:
            threatLevel += 3
        elif humidity >= 31 and humidity <= 50:
            threatLevel += 2
        elif humidity < 30:
            threatLevel += 1

        if windSpeed < 40:
            threatLevel += 3
        elif windSpeed >= 41 and windSpeed <= 55:
            threatLevel += 2
        elif windSpeed > 55:
            threatLevel += 1
        dataHeap.insert(threatLevel, vert.getLabel())
    return dataHeap

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
    
    print("------[DFS]-----------------")
    #testing DFS
    print("DFS from A:")
    path, distance = uav.DFS("A")
    pathArray = ezFlightParse(path)
    print("DFS path: ", pathArray)
    print("Distance: ", distance)
    print("------[parseToTable]--------")
    #parsing flight path to hash table
    table = uav.pathToTable(path)
    for item in table.displayTable():
        if item.getValue() is not None:
            #skip empty indexes
            print(item.getKey(), item.getValue())
    
    print("------[Heaping]-------------")
    dataHeap = threatTracker(uav, "A")
    #testing heap
    for item in dataHeap.heap:
        print(item.getValue(), end = " ")
    print()

    print("------[Itinerary]-----------")
    #testing itinerary
    dangerPath = dataHeap.export() 
    #find the high risk areas (lower number, the higher the risk)
    #remove excess items (anything over 5)
    for i in range(len(dangerPath)):
        if dangerPath[i][0] > 5:
            dangerPath[i] = None
    print(dangerPath)

    print("------[Flight]--------------")
    for i in range(len(dangerPath)):
        try:
            if dangerPath[i + 1] is not None:
                path, distance = uav.travel(dangerPath[i][1], dangerPath[i + 1][1])
                path = ezFlightParse(path)
                print("Flight path: ", path)
                print("Distance: ", distance)
        except IndexError:
            pass

    print("------[End]-----------------")

if __name__ == "__main__":
    main()