import Dependancies.DSAGraph as DSAGraph
import Dependancies.DSALinkedList as ll
import sys
import time

def main():
    '''
    scalability program to create, edit, and remove vertices and edges
    '''
    
    print("------\n Running: Scalabiltiy Program\n------")
    '''
    possible choices
    - import file : 
    - export file :
    - add vertex : 
    - add edge : 
    - remove vertex : 
    - remove edge : 
    - display as list : 
    - edit weight of edge :
    - find edge : 
    '''

    #init objects
    graph = DSAGraph.Graph()
    userInput = (None, None)
    while userInput[0] != "q":
        userInput = input("> ").split()

        if userInput[0] == "help":
            print("help: ")
            print("import <location file> <data file>")
            print("add <vertex label> <vertex value>")
            print("addEdge <vertex1> <vertex2> <weight>")
            print("remove <vertex label>")
            print("removeEdge <vertex1> <vertex2>")
            print("edit <vertex>")
            print("display")

        elif userInput[0] == "import":
            locationPath = userInput[1]
            dataPath = userInput[2]
            graph.importFile(locationPath, dataPath)
            print("imported")

        elif userInput[0] == "add": #would look like add A 12 13 14
            label = userInput[1]
            
            value = userInput[1:]
            #if userInput was "add 12 13 14"
            #then value would be [12, 13, 14]
            graph.addVertex(label, tuple(value))
            print(f"added vertex {label} with value {value}")

        elif userInput[0] == "addEdge":
            vertex1 = userInput[1]
            vertex2 = userInput[2]
            weight = userInput[3]
            graph.addTwoWay(vertex1, vertex2, weight)
            print(f"added edge between {vertex1} and {vertex2} with weight {weight}")
        
        elif userInput[0] == "remove":
            label = userInput[1]
            graph.removeVertex(label)
            print(f"removed vertex {label}")

        elif userInput[0] == "removeEdge":
            vertex1 = userInput[1]
            vertex2 = userInput[2]
            graph.removeEdge(vertex1, vertex2)
            print(f"removed edge between {vertex1} and {vertex2}")

        elif userInput[0] == "edit":
            vertex = graph.getVertex(userInput[1])
            editVertex(graph, vertex)

        elif userInput[0] == "find":
            #find userInput[1]
            try:
                graph.getVertex(userInput[1])
                print(f"vertex {userInput[1]} found")
            except ValueError:
                print(f"vertex {userInput[1]} not found")

        elif userInput[0] == "display":
            graph.displayAsList()

        else:
            print("Error: invalid input")
            
    print("exiting")

def editVertex(graph:DSAGraph.Graph, vertexObject:DSAGraph.GraphVertex):
    '''
    methods:
    - edit label :
    - edit value :
    - remove edges :
    - add edges :
    '''
    userInput = (None, None)
    while userInput[0] != "q":
        userInput = input(f"editing {vertexObject.getLabel()} -> ").split()
        if userInput[0] == "help":
            print("help: ")
            print("label <new label>")
            print("value <new value>")
            print("addEdge <vertex2> <weight>")
            print("removeEdge <vertex2>")
            print("display")
    
        elif userInput[0] == "label":

            #check if label already exists
            try:
                graph.getVertex(userInput[1])
                print(f"vertex {userInput[1]} already exists")
                return
            except ValueError:
                ...

            vertexObject.setLabel(userInput[1])

        elif userInput[0] == "value":
            vertexObject.setValue(userInput[1])

        elif userInput[0] == "addEdge":
            vertex2 = userInput[1]
            weight = userInput[2]
            try:
                graph.addTwoWay(vertexObject.getLabel(), vertex2, weight)
            except ValueError:
                print(f"vertex {vertex2} not found")

        elif userInput[0] == "removeEdge":
            vertex2 = userInput[1]
            try:
                graph.removeEdge(vertexObject.getLabel(), vertex2)
            except ValueError:
                print(f"vertex {vertex2} not found")

        elif userInput[0] == "display":
            print(vertexObject)

def quickTest():
    graph = DSAGraph.Graph()
    graph.importFile("txtFiles/location.txt", "txtFiles/UAVdata.txt")
    '''
    testing methods
    - add vertex : 
    - add edge : 
    - remove vertex : 
    - remove edge : 
    - edit weight of edge : 
    '''
    print("---running quick test---")
    try: #trying to add a vertex
        graph.addVertex("New", "NewItem created by test")
        print("add vertex test passed")
    except Exception as e:
        print("add vertex test failed with error: " + str(e))
        
    try: #trying to add an edge
        graph.addTwoWay("A", "G", 1)
        print("add edge test passed")
    except Exception as e:
        print("add edge test failed with error: " + str(e))

    try: #trying to remove a vertex
        graph.removeVertex("New")
        print("remove vertex test passed")
    except Exception as e:
        print("remove vertex test failed with error: " + str(e))

    try: #trying to remove an edge
        graph.removeEdge("A", "G")
        print("remove edge test passed")
    except Exception as e:
        print("remove edge test failed with error: " + str(e))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        main()
    if sys.argv[1] == '-q':
        quickTest()
    