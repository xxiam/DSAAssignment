#using graph, hash table, heap
import Dependancies.DSAGraph as DSAGraph
import Dependancies.DSAhash as DSAhash
def main():

    #A 32 45 90
    #location : temperature, humidity, wind speed

    graph = DSAGraph.Graph()
    hashTable = DSAhash.DSAHashTable(graph.getVertCount())
    graph.importFile("location.txt", "UAVdata.txt") #finished importing
    print("Graph adjaceny list")
    graph.displayAsList()

    #create flight path and store data in hash table
    print("traversing from A to D")
    flightPath = graph.dijkstra("A", "D")
    distance = 0
    for vertex, weight in iter(flightPath):
        print(vertex.getLabel(), weight)
        distance += float(weight)
    print("Total distance: ", distance)

if __name__ == "__main__":
    main()