
import DSALinkedList as ll

'''
DSAGraph - self.vertices will be using linked lists
linked list value will be DSAGraphVertex
DSAGraphVertex linkes will be using linked lists
'''

class DSAGraphVertex():

    def __init__(self, label, value):
        self.value = value
        self.label = label
        self.linksList = ll.DSALinkedList()
        self.visited = False

    def getValue(self):
        return self.value

    def getLabel(self):
        return self.label

    def getLinks(self):
        return iter(self.linksList)

    def setValue(self, value):
        self.value = value
    
    def addEdge(self, vertex): #vertex is passed in as a DSAGraphVertex object
        self.linksList.insertFirst(vertex)

    def clearVisited(self):
        self.visited = False

    def setVisited(self):
        self.visited = True
        return self.visited

    def isVisited(self):
        return self.visited

    def allVisited(self):
        for links in iter(self.linksList):
            if links.isVisited() is True:
                return True
        else:
            return False



    def __str__(self):
        return (f"Label: {self.getLabel()} | Value: {self.getValue()}")

class DSAGraph(DSAGraphVertex):

    def __init__(self):
        self.vertCount = 0
        self.linkCount = 0
        self.vertices = ll.DSALinkedList()

    def addVertex(self, label, value):
        '''
        inserts new vertex into the list
        returning newVertex allows the object to be bound to a variable and be mutated directly, rather than having to access self.vertices
        '''
        newVertex = DSAGraphVertex(label, value)
        self.vertices.insertLast(newVertex)
        self.vertCount += 1
        return newVertex

    def addEdge(self, label1, label2):
        '''
        adds a connection between two vertices
        '''
        self.linkCount += 2
        label1 = self.getVertex(label1)
        label2 = self.getVertex(label2)
        label1.addEdge(label2)
        label2.addEdge(label1)

    def addOneWay(self, label1, label2):
        '''
        adds a one way connection from label1 to label2
        '''
        self.linkCount += 1
        label1 = self.getVertex(label1)
        label2 = self.getVertex(label2)
        label1.addEdge(label2)

    def hasVertex(self, label):
        for value in iter(self.vertices):
            if label == value.getLabel():
                return True
        else: 
            return False

    def getVertexCount(self):
        return self.vertCount
            
    def getEdgeCount(self):
        return self.linkCount
    
    def getVertex(self, label):
        for vertex in iter(self.vertices):
            if label == vertex.getLabel():
                return vertex

    def getAdjacent(self, label):
        for vertex in iter(self.vertices):
            if vertex.getLabel() ==  label:
                return iter(vertex.linksList)
            else:
                raise ValueError("Error: no such vertex: " + label)
    
    def isAdjacent(self, label1, label2):
        for value in iter(label1.linksList):
            if value == label2:
                return True
        else:
            return False
        
    def displayAsList(self):
        for value in iter(self.vertices):
            print(f"Vertex {value.getLabel()} links: ", end = "")
            for vert in iter(value.linksList):
                print(f"{vert.getLabel()} ", end = "")
            print("")

    def displayAsMatrix(self):
        print("v", end = "\t")
        #prints column labels for matrix
        for value in iter(self.vertices):
            print(f"{value.getLabel()}", end = "\t")
        print('')
        #fills out the rows according to adjacency
        tempList = list(iter(self.vertices)) #weird interaction where nested for loops break, new solution
        for vert in tempList:
            print(f"{vert.getLabel()}", end = "\t")
            for nextVert in tempList:
                if self.isAdjacent(vert, nextVert) is True:
                    print("1", end = "\t")
                else:
                    if vert is nextVert:
                        print("x", end = "\t")
                    else:
                        print("0", end = "\t")
            print("")

    def unvisitAll(self):
        for vert in iter(self.vertices):
            vert.visited = False

    def DFS(self):
        self.unvisitAll()
        t = ll.DSALinkedList()
        return self.__DFS(t, self.vertices.peekFirst())

    def __DFS(self, t, currentVert):
        if currentVert.isVisited() is False:
            t.insertLast(currentVert)
            currentVert.setVisited()
            for adj in iter(currentVert.linksList):
                self.__DFS(t, adj)
        return t
        
    def BFS(self):
        self.unvisitAll()
        t = ll.DSALinkedList()
        queue = ll.DSALinkedList()
        return self.__BFS(queue, t, self.vertices.peekFirst())
    
    def __BFS(self, queue, t, currentNode):
        currentNode.setVisited()
        queue.insertLast(currentNode)
    
        while queue.isEmpty() is False:
            cVert = queue.removeFirst()

            for adj in iter(cVert.linksList):
                if adj.isVisited() is False:
                    t.insertLast((cVert, adj))
                    adj.setVisited()
                    queue.insertLast(adj)
        return t

    # do export and import
    
if __name__ == "__main__":
    def testFunc():
        g = DSAGraph()
        test1 = g.addVertex(3, "testing")
        test2 = g.addVertex(5, "value")
        test3 = g.addVertex(7, "another value")

        print("Printing current vertices ---")
        myiter = iter(g.vertices)
        for value in myiter:
            print(value)
        print("---")
        g.addEdge(3, 5)
        g.addEdge(5, 7)

        print("Printing test1's links ---")
        for value in iter(test1.linksList):
            print(value)
        print("---\nPrinting edge count of graph ---")
        print(g.getEdgeCount())
        print("---\nPrinting vertice count of graph ---")
        print(g.getVertexCount())
        print("---\nIs adjacent test ---")
        print(g.isAdjacent(test1, test3))
        print(g.isAdjacent(test1, test2))   
        print("---\nPrinting as adjacency list ---")
        g.displayAsList()
        print("---\nPrinting as adjacency matrix ---")
        g.displayAsMatrix()
        print("--- BFS --")
        for item in iter(g.BFS()):
            print(f"{item[0]} to {item[1]}")
        print("-----")
        print(g.getVertex(5))
        g.getAdjacent(100)
    testFunc()