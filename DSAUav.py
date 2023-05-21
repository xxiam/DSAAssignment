import Dependancies.DSAGraph as DSAGraph
import Dependancies.DSAhash as DSAhash
import Dependancies.DSAHeap as DSAHeap
import Dependancies.DSALinkedList as DSALinkedList

class UAV:
    def __init__(self):
        self.uav = DSAGraph.Graph()
        self.location = None

    def importFile(self, locationPath, dataPath):
        self.uav.importFile(locationPath, dataPath)
    
    def travel(self, start, end):
        if start is None:
            start = self.location
        if end is None:
            raise ValueError("End location cannot be None")

        flightPath = self.uav.dijkstra(start, end)
        distance = 0
        for vertex, weight in iter(flightPath):
            distance += float(weight)
        self.location = end
        return flightPath, distance
    
    def display(self):
        self.uav.displayAsList()

    def hamiltonianCycle(self, start):
        return self.uav.hamiltonianCycle(start)
    
    def pathToTable(self, path:DSALinkedList.DSALinkedList):
        table = DSAhash.DSAHashTable()
        for vert, weight in iter(path):
            table.put(vert.getLabel(), vert.getValue())
        return table