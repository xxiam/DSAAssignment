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

    def addOneWay(self, label1, label2, weight):
        label1 = self.getVertex(label1)
        label2 = self.getVertex(label2)

        label1.addEdge(label2, weight)

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

    def DFS(self, start, finish):
        '''
        Depth First Search
        '''
        start = self.getVertex(start)
        finish = self.getVertex(finish)
        start.visit()
        if start == finish:
            return True
        else:
            for links, weight in iter(start.getLinks()):
                if links.isVisited() is False:
                    if self.DFS(links.getLabel(), finish.getLabel()) is True:
                        return True
        return False
    
    def BFS(self, start, finish):
        '''
        Breadth First Search
        '''
        start = self.getVertex(start)
        finish = self.getVertex(finish)
        start.visit()
        queue = ll.DSALinkedList()
        queue.insertLast(start)
        while queue.isEmpty() is False:
            current = queue.removeFirst()
            if current == finish:
                return True
            else:
                for links, weight in iter(current.getLinks()):
                    if links.isVisited() is False:
                        links.visit()
                        queue.insertLast(links)
        return False
    
    def importFile(self, filename):
        #line 1 is how many vertices and edges there are
        with open(filename, 'r') as data:
            vertCount, edgeCount = data.readline().split()
            for i in range(int(edgeCount)):
                label1, label2, weight = data.readline().split()
                self.addVertex(label1, None)
                self.addVertex(label2, None)
                self.addTwoWay(label1, label2, weight)

def test():
    graph = Graph()
    graph.importFile("location.txt")

if __name__ == "__main__":
    test()