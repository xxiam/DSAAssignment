
import Dependancies.DSAGraph as DSAGraph

#create graph and test search alg

def test():
    graph = DSAGraph.Graph()
    graph.importFile("txtFiles/location.txt", "txtFiles/UAVdata.txt")
    graph.displayAsList()
    
    print("dijkstra's algorithm")
    for item, weight in graph.dijkstra("A", "F"):
        print(item.getLabel(), end = ' ')
    print()

if __name__ == "__main__":
    test()
    
#--------------------
