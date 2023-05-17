#using graph, hash table, heap
import DSAGraph

def main():

    #A 32 45 90
    #location : temperature, humidity, wind speed


    graph = DSAGraph.Graph()
    graph.importFile("location.txt", "UAVdata.txt") #finished importing

    graph.sortVertices()

if __name__ == "__main__":
    main()