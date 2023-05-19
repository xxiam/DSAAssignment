import Dependancies.DSAGraph as DSAGraph
import Dependancies.DSAhash as DSAhash

class UAV:
    def __init__(self, location, data):
        #import data
        self.uavLocation = DSAGraph.Graph().importFile(location, data)
        #uavLocation has all locations and data associated with location

    def getLocation(self):
        return self.uavLocation
    
    def travel(self, start, end):
        table = DSAhash.DSAHashTable(self.uavLocation.getVertCount())
        path = self.uavLocation.traverse(start, end)
        #put data into hash table
        for vertex, weight in iter(path):
            table.put(vertex.getLabel(), vertex.getValue())
        return table
    
    def shortPath(self, start):
        #find shortest path from start to all other locations
        ...