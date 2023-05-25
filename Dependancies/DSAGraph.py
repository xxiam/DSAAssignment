import Dependancies.DSALinkedList as ll
import Dependancies.DSAHeap as heap
import Dependancies.DSAhash as hashTable
import numpy as np
import DSAUav

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
    
    def setLabel(self, label):
        self.label = label

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

    def getVertCount(self):
        return self.vertCount
    def getEdgeCount(self):
        return self.linkCount

    def unvisitAll(self):
        for vertex in iter(self.vertices):
            vertex.unvisit()

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
                raise ValueError(f"Vertex with label {label} already exists")
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
        self.linkCount += 1

    def displayAsList(self):
        for item in iter(self.vertices):
            print(f"{item.getLabel()} |: ", end = ' ')
            for links in item.getLinks():
                print(links[0].getLabel(), end = ' ')
                print(links[1], end = ' | ')
            print()

#search algorithms
#DFS finds the shortest path between thw whole graph, does not consider weight
#dijkstra finds the shortest path between two locations, considering weight
#A* finds the shortest path between two locations, considering weight and heuristic
    #------------------------------------------

    def traverse(self, start, finish):
        start = self.getVertex(start)
        finish = self.getVertex(finish)

        return self.traverseAlg(start, finish)

    def traverseAlg(self, start, finish):
        queue = ll.DSALinkedList()
        path = ll.DSALinkedList()
        self.unvisitAll()

        #start
        currentVert = start
        currentVert.visit()
        queue.insertFirst(currentVert)
        path.insertFirst((currentVert, 0))

        while queue.isEmpty() is False:
            currentVert = queue.removeFirst()
            for links, weight in iter(currentVert.getLinks()):
                if links.isVisited() is False:
                    links.visit()
                    queue.insertFirst(links)
                    path.insertLast((links, weight))
                    if links == finish:
                        return path
        else:
            return path

    def DFS(self, start):
        '''
        traverse the whole grpah following the lowest weight
        '''
        start = self.getVertex(start)
        self.unvisitAll()
        return self.DFSAlg(start)
    
    def DFSAlg(self, start):
        path = ll.DSALinkedList()
        stack = ll.DSALinkedList()
        start.visit()
        path.insertFirst((start, 0)) #start has 0 weight
        stack.insertFirst(start)

        while stack.isEmpty() is False:
            currentVert = stack.removeFirst()
            for links, weight in iter(currentVert.getLinks()):
                if links.isVisited() is False:
                    links.visit()
                    stack.insertFirst(links)
                    path.insertLast((links, weight))
        return path
# ------------------------------------------

    def dijkstra(self, start:str, end:str):
        start = self.getVertex(start)
        end = self.getVertex(end)

        return self.dijkstraAlg(start, end)
    
    def dijkstraAlg(self, start:GraphVertex, end:GraphVertex):
        self.unvisitAll()
        '''
        Dijkstra's algorithm
        '''
        distances = {vertex: float('infinity') for vertex in iter(self.vertices)}
        distances[start] = 0
        priorityQueue = heap.DSAHeap(self.getVertCount())
        priorityQueue.insert(0, start)
        previous = {vertex: None for vertex in iter(self.vertices)}

        while priorityQueue.isEmpty() is False:
            currentDistance, currentVertex = priorityQueue.remove()

            #skip if found better path to curentVertex
            if currentDistance > distances[currentVertex]:
                continue

            if currentVertex == end:
                break

            for links, weight in iter(currentVertex.getLinks()):
                distance = float(currentDistance) + float(weight)

                #skip if found better path to links
                if distance < distances[links]:
                    distances[links] = distance
                    previous[links] = currentVertex
                    priorityQueue.insert(distance, links)

        path = ll.DSALinkedList()
        while currentVertex is not None:
            path.insertFirst((currentVertex, distances[currentVertex]))
            currentVertex = previous[currentVertex]
        return path
    
    #experimental aStar

    def aStar(self, start, end):
        '''
        A* search algorithm
        '''
        start = self.getVertex(start)
        end = self.getVertex(end)

        return self.aStarAlg(start, end)
    
    def aStarAlg(self, start, end):
        '''
        A* search algorithm
        '''
        distances = {}
        previous = {}
        nodes = heap.DSAHeap(self.getVertCount())
        path = ll.DSALinkedList()

        for vertex in iter(self.vertices):
            if vertex == start:
                distances[vertex] = 0
                nodes.insert(0, vertex)
            else:
                distances[vertex] = np.inf
                nodes.insert(np.inf, vertex)
            previous[vertex] = None

        while nodes.isEmpty() is False:
            smallest = nodes.remove()
            if smallest == end:
                while previous[smallest] is not None:
                    path.insertFirst((smallest, distances[smallest]))
                    smallest = previous[smallest]
                break

            if distances[smallest] == np.inf:
                break

            for links, weight in iter(smallest.getLinks()):
                alt = distances[smallest] + weight
                if alt < distances[links]:
                    distances[links] = alt
                    previous[links] = smallest
                    nodes.insert(alt, links)

        return path
    
    #------------------------------------------

#search algorithms

    def importFile(self, filename, uavData): #uavData looks like (location, temp, humidity, windspeed) separated by spaces
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

            #validating the data
            if self.getVertCount() != int(vertCount):
                raise ValueError("Error: vertex count does not match")
            if self.getEdgeCount() != int(edgeCount):
                raise ValueError("Error: edge count does not match")
            
            with open(uavData, 'r') as f:
                for i in range(int(vertCount)):
                    vertex, temp, humidity, speed = np.array(f.readline().strip().split())
                    vertex = self.getVertex(vertex)
                    locationData = DSAUav.Location(temp, humidity, speed)
                    vertex.setValue(locationData)
        except FileNotFoundError:
            raise FileNotFoundError("Error: " + filename + " does not exist")
        
        return vertCount
    
    #testing remove

    def removeEdge(self, vert1:str, vert2:str):
        vert1 = self.getVertex(vert1)
        vert2 = self.getVertex(vert2)

        for links, weight in iter(vert1.getLinks()):
            if links == vert2:
                vert1.links.removeItem((links, weight))
                self.linkCount -= 1
        #can be improved
        for links, weight in iter(vert2.getLinks()):
            if links == vert1:
                vert2.links.removeItem((links, weight))
                self.linkCount -= 1

    def removeVertex(self, vert:str):
        vertex = self.getVertex(vert)

        #remove any links to this vertex
        if vertex.links.isEmpty() is not None:
            for links, weight in iter(vertex.getLinks()):
                self.removeEdge(vert, links.getLabel())
        
        #remove vertex
        self.vertices.removeItem(vertex)