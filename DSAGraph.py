import DSALinkedList as ll
import numpy as np
'''
quick rewrite of DSAGraph.py, modified to allow weighted edges
and better search algorithms
'''

class GraphVertex():

    def __init__(self, label, value):
        self.value = value
        self.label = label
        self.links = ll.DSALinkedList() #links look like [(vertex, weight), (vertex, weight)]
        self.visited = False

    def getValue(self):
        return self.value
    
    def getLabel(self):
        return self.label
    
    def getLinks(self):
        return iter(self.links)
    
    def setValue(self, value):
        self.value = value

    def addEdge(self, vertex, weight):
        self.links.insertFirst(vertex, weight) #can be changed to an np.arry if needed
    
    def unvisit(self):
        self.visited = False
    
    def visit(self):
        self.visited = True

    def isVisited(self):
        return self.visited
    
    def allVisited(self):
        for links, weight in iter(self.links): #skip weight
            if links.isVisited() is True:
                return True
            
    def __str__(self):
        return (f"Label: {self.getLabel()} | Value: {self.getValue()} | Visited: {self.isVisited()}")
    
class Graph(GraphVertex):

    def __init__(self):
        self.vertCount = 0
        self.linkCount = 0
        self.vertices = ll.DSALinkedList()

    def getVertCount(self):
        return self.vertCount
    def getEdgeCount(self):
        return self.linkCount

    def isVertex(self, item):
        #check vertice list if item is already a vertex
        for vertex in iter(self.vertices):
            if vertex.getLabel() == item:
                return True
        else:
            return False

    def hasVertex(self, item):
        #check vertice list if item is already a vertex
        for vertex in iter(self.vertices):
            if vertex.getLabel() == item:
                return vertex
        else:
            return False

    def addVertex(self, label, value):
        #check if vertex already exists
        for vertex in iter(self.vertices):
            if vertex.getLabel() == label:
                #overwrite its value
                vertex.setValue(value)
        else:
            self.vertices.insertFirst(GraphVertex(label, value))
            self.vertCount += 1

    def getVertex(self, label):
        for vertex in iter(self.vertices):
            if vertex.getLabel() == label:
                return vertex
        else:
            raise ValueError(f"Vertex with label {label} not found")
        
    def addTwoWay(self, label1, label2, weight):
        label1 = self.getVertex(label1)
        label2 = self.getVertex(label2)

        label1.addEdge(label2, weight)
        label2.addEdge(label1, weight)
        self.linkCount += 2

    def addOneWay(self, label1, label2, weight):
        label1 = self.getVertex(label1)
        label2 = self.getVertex(label2)

        label1.addEdge(label2, weight)
        self.linkCount += 1

    def removeEdge(self, label1, label2):
        '''
        removes label1's connection to label2, but not the other way around
        '''
        label1 = self.getVertex(label1)
        label2 = self.getVertex(label2)
        
        label1.removeItem(label2)
        
    def removeVertex(self, label):
        '''
        removes a vertex from the graph, and all connections to it
        '''
        for vertex in iter(self.vertices):
            vertex.removeItem(label)
        self.vertices.removeItem(label)
        self.vertCount -= 1

    def displayAsList(self):
        for item in iter(self.vertices):
            print(f"{item.getLabel()} |: ", end = ' ')
            for links in item.getLinks():
                print(links[0].getLabel(), end = ' ')
                print(links[1], end = ' | ')
            print()

#search algorithms

#BFS finds the shortest path between two locations
#DFS explores the whole graph in the shortest amount of distance

#search algorithms

    def importFile(self, filename):
        #line 1 is how many vertices and edges there are
        try:
            with open(filename, 'r') as f:
                vertCount, edgeCount = f.readline().split()
                for i in range(int(edgeCount)):
                    #in order of items, vertex1, vertex2, weight
                    data = np.array(f.readline().split('\n')[0].split())
                    
                    #create verticies
                    if self.isVertex(data[0]) is False:
                        self.addVertex(data[0], None)
                    if self.isVertex(data[1]) is False:
                        self.addVertex(data[1], None)

                    #add edges
                    self.addTwoWay(data[0], data[1], data[2])
        except FileNotFoundError:
            raise FileNotFoundError("Error: " + filename + " does not exist")
                
def test():
    graph = Graph()
    graph.importFile("location.txt")

if __name__ == "__main__":
    test()