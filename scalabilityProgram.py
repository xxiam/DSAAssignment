import Dependancies.DSAGraph as DSAGraph
import sys

def main():
    '''
    scalability program to create, edit, and remove vertices and edges
    '''
    
    print("Scalabiltiy Program")
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
    '''

    #init objects
    graph = DSAGraph.Graph()
    userInput = (None, None)
    while userInput[0] != "q":
        userInput = input("> ").split()

        if userInput[0] == "help":
            print("help: ")
            print("import <location file> <data file>")
            print("export <location filename> <data filename>")
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

        elif userInput[0] == "export":
            #create export method in DSAgraph.py
            ...

        elif userInput[0] == "add":
            label = userInput[1]
            value = userInput[2]
            graph.addVertex(label, value)

        elif userInput[0] == "addEdge":
            vertex1 = userInput[1]
            vertex2 = userInput[2]
            weight = userInput[3]
            graph.addTwoWay(vertex1, vertex2, weight)
        
        elif userInput[0] == "remove":
            label = userInput[1]
            graph.removeVertex(label)

        elif userInput[0] == "removeEdge":
            vertex1 = userInput[1]
            vertex2 = userInput[2]
            graph.removeEdge(vertex1, vertex2)

        elif userInput[0] == "edit":
            editVertex(userInput[1])

        elif userInput[0] == "display":
            graph.displayAsList()

    print("exiting")

def editVertex(vertexObject:DSAGraph.GraphVertex):
    ...

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
    