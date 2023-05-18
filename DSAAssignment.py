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

if __name__ == "__main__":
    main()