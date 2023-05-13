#using graph, hash table, heap
import DSAGraph

def main():
    graph = DSAGraph.Graph()
    graph.importFile("location.txt")

    print(graph.getVertCount())
    print(graph.getEdgeCount())

if __name__ == "__main__":
    main()