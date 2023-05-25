#using graph, hash table, heap

import Dependancies.DSAGraph as DSAGraph
import Dependancies.DSAhash as DSAhash
import Dependancies.DSAHeap as DSAHeap
import Dependancies.DSALinkedList as DSALinkedList
import numpy as np
import DSAUav
import sys

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

def quickTest():
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
    #create subtree from high risk areas
    #create new array

    #given our location is at A, remove other locations, except for locations in dangerPath
    c = 0
    for item in dangerPath:
        if item is not None:
            c += 1
    
    path = np.empty(c, dtype = object) #this is the array to use
    for i in range(len(dangerPath)):
        if dangerPath[i] is not None:
            path[i] = dangerPath[i]

    #find shortest path to start with
    start = "A"

    travelPath = DSAHeap.DSAHeap(len(path))

    for t, vert in path:
        #add to heap
        p, dist = uav.travel(start, vert)
        travelPath.insert(dist, vert)
    
    totalDistance = 0
    while travelPath.isEmpty() is False:
        _, dest = travelPath.remove()
        _, distance = uav.travel(start, dest)
        totalDistance += distance
    
    print(f"total distance travelled: {totalDistance}")

    print("------[End]-----------------")

def main(UAVloaction:str, UAVdata:str):
    '''
    interactive menu for UAV
    '''
    
    #import file into uav object
    uav = DSAUav.UAV()
    uav.importFile(UAVloaction, UAVdata)
    print(f"imported {UAVloaction} and {UAVdata}")
    
    print("---[Interactive Menu for UAV]---")
    userInput = (None, None)
    while userInput != "q":
        userInput = input("> ")

        if userInput == "h": 
            print("> importFile <location> <data> : imports a new map for the uav")
            print("> travel <start> <dest> : uses dijkstra's algorithm to find the shortest path")
            print("> display : displays adjacency list")
            print("> hamiltonianCycle <start> : WIP")
            print("> DFS <start> : generic prac6 DFS")
            print("> itinerary <start> : create flight path based on threat level")

        elif userInput == "display":
            uav.display()
        
        try:
            userInput = userInput.split()
        except:
            pass

        if userInput[0] == "importFile":
            location = userInput[1]
            data = userInput[2] 
            uav.importFile(location, data)
            print("imported !")
        
        elif userInput[0] == "travel":
            start = userInput[1]
            dest = userInput[2]
            path, distance = uav.travel(start, dest)
            path = ezFlightParse(path)
            print(f"Flight path: {path}")
            print(f"Distance: {distance}")

        elif userInput[0] == "hamiltonianCycle":
            ...

        elif userInput[0] == "DFS":
            path, distance = uav.DFS(userInput[1])
            path = ezFlightParse(path)
            print(f"Flight path: {path}")
            print(f"Distance: {distance}")
        
        elif userInput[0] == "itinerary":
            start = userInput[1]

            dataHeap = threatTracker(uav, start)
            dataHeap = dataHeap.export()
            #create itinerary
            for i in range(len(dataHeap)):
                if dataHeap[i][0] > 5:
                    dataHeap[i] = None
            
            #shorten array
            c = 0
            for item in dataHeap:
                if item is not None:
                    c += 1
                
            path = np.empty(c, dtype = object)
            for i in range(len(dataHeap)):
                if dataHeap[i] is not None:
                    path[i] = dataHeap[i]
            
            travelPath = DSAHeap.DSAHeap(len(path))
            for t, vert in path:
                _, dist = uav.travel(start, vert)
                travelPath.insert(dist, vert)
            
            totalDistance = 0
            while travelPath.isEmpty() is False:
                _, dest = travelPath.remove()
                _, distance = uav.travel(start, dest)
                totalDistance += distance
            
            print(f"total distance travelled: {totalDistance}")
        
        else:
            print("Error: invalid input")

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "-i":
        main("txtFiles/location.txt", "txtFiles/UAVdata.txt")
    elif len(sys.argv) == 2 and sys.argv[1] == "-q":
        quickTest()
    
    else:
        print("usage: python3 DSAAssignment.py [option]")
        print("-q : quick test, testing methods")
        print("-i : interactive mode")
