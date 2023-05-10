import DSALinkedList as ll

'''
quick rewrite of DSAGraph.py, modified to allow weighted edges
and better search algorithms
'''

class GraphVertex():

    def __init__(self, label, value):
        self.value = value
        self.label = label
        self.links = ll.DSALinkedList()
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
        self.links.insertFirst((vertex, weight)) #can be changed to an np.arry if needed
    
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

    def addVertex(self, label, value):
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

    def addOneWay(self, label1, label2, weight):
        label1 = self.getVertex(label1)
        label2 = self.getVertex(label2)

        label1.addEdge(label2, weight)

    def removeEdge(self, label1, label2):
        '''
        removes an edge between two vertices
        '''
        label1 = self.getVertex(label1)
        label2 = self.getVertex(label2)
        