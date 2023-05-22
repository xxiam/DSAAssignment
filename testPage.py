
import Dependancies.DSAGraph as DSAGraph

#create graph and test search alg

def test():
    graph = DSAGraph.Graph()
    graph.addVertex("A", "value")
    graph.addVertex("B", "another value")
    graph.addVertex("C", "yet another value")
    graph.addVertex("D", "yet another value")
    graph.addTwoWay("A", "B", 1)
    graph.displayAsList()
    print("removing vertex--")
    graph.removeVertex("A")
    graph.displayAsList()
    


if __name__ == "__main__":
    test()
    
#--------------------
