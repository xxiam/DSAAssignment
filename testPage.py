
import Dependancies.DSAGraph as DSAGraph

#create graph and test search alg

graph = DSAGraph.Graph()

graph.importFile("location.txt", "UAVData.txt")
graph.displayAsList()