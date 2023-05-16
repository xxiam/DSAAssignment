#using graph, hash table, heap
import DSAGraph

def main():

    #A 32 45 90
    #location : temperature, humidity, wind speed


    graph = DSAGraph.Graph()
    graph.importFile("location.txt") #finished importing

    graph.displayAsList()

if __name__ == "__main__":
    main()