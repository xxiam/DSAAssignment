import Dependancies.DSAGraph as DSAGraph
import Dependancies.DSAhash as DSAhash
import Dependancies.DSAHeap as DSAHeap
import Dependancies.DSALinkedList as DSALinkedList

class UAV:
    def __init__(self):
        self.uav = DSAGraph.Graph()
        self.locationCount = None

    def importFile(self, locationPath, dataPath):
        try:
            self.locationCount = int(self.uav.importFile(locationPath, dataPath))
        except FileNotFoundError as e:
            print(e)
    
    def travel(self, start, end):
        try:
            flightPath = self.uav.dijkstra(start, end)
            distance = flightPath.peekLast()[1]
            return flightPath, distance
        except ValueError as e:
            print(e)
    
    def display(self):
        self.uav.displayAsList()

    def hamiltonianCycle(self, start):
        return self.uav.hamiltonianCycle(start)
    
    def pathToTable(self, path:DSALinkedList.DSALinkedList):
        table = DSAhash.DSAHashTable()
        for vert, weight in iter(path):
            table.put(vert.getLabel(), vert.getValue())
        return table
    
    def DFS(self, start):
        try:
            path = self.uav.DFS(start)
            distance = 0
            for vertex, weight in iter(path):
                distance += float(weight)
            return path, distance
        except ValueError as e:
            print(e)
        
    
class Location:
    def __init__(self, temperature, humidity, windSpeed):
        self.temperature = temperature
        self.humidity = humidity
        self.windSpeed = windSpeed
    
    #getters
    def getTemperature(self):
        return self.temperature
    
    def getHumidity(self):
        return self.humidity
    
    def getWindSpeed(self):
        return self.windSpeed