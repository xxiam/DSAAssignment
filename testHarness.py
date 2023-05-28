'''
test harness for all files
'''
import string
import Dependancies.DSAGraph as DSAGraph
import Dependancies.DSAhash as DSAHashTable
import Dependancies.DSAHeap as DSAHeap
import Dependancies.DSALinkedList as DSALinkedList
import DSAUav

'''
classes to test:
    Graph
    DSAHashTable
    DSAHeap
    DSALinkedList
    DSAUav
'''

print(f"---Test Harness---")
print("Method\t\tStatus")

#testing graph
print("---[DSAGraph]---")
graph = DSAGraph.Graph()
try:
    graph.importFile("txtFiles/location.txt", "txtFiles/UAVdata.txt")
    print("importFile\tpassed")
except FileNotFoundError as e:
    print("import\t\tfailed\t" + e)

try:
    if graph.getVertCount() == 10:
        print("getVertCount\tpassed")
    else:
        raise ValueError
except ValueError:
    print("getVertCount\tfailed")

try:
    if graph.getEdgeCount() == 15:
        print("getEdgeCount\tpassed")
    else:
        raise ValueError
except ValueError:
    print("getEdgeCount\tfailed")

try:
    for i in range(graph.getVertCount()):
        status = graph.hasVertex(string.ascii_uppercase[i])
        if status is False:
            raise ValueError
    print("hasVertex\tpassed")
except ValueError:
    print("hasVertex\tfailed")

try:
    graph.addVertex("K", (10, 10, 10))
    print("addVertex\tpassed")
except:
    print("addVertex\tfailed")

try:
    for i in range(graph.getVertCount()):
        status = graph.getVertex(string.ascii_uppercase[i])
        if status is False:
            raise ValueError
    print("getVertex\tpassed")
except ValueError:
    print("getVertex\tfailed")

try:
    graph.addTwoWay("A", "K", 3.2)
    print("addTwoWay\tpassed")
except:
    print("addTwoWay\tfailed")

try:
    path = graph.DFS("A")
    if path is None:
        raise ValueError
    print("DFS\t\tpassed")
except ValueError:
    print("DFS\t\tfailed")

try:
    path = graph.dijkstra("A","G")
    if path is None:
        raise ValueError
    print("dijkstra\tpassed")
except ValueError:
    print("dijkstra\tfailed")

try:
    graph.removeVertex("A")
    graph.removeVertex("B")
    graph.removeVertex("C")
    print("removeVertex\tpassed")
except:
    print("removeVertex\tfailed")

print("---[Hash Table]---")
ht = DSAHashTable.DSAHashTable()
try:
    ht.put("Z", "value")
    print("put\t\tpassed")
except:
    print("put\t\tfailed")

try:
    ht.get("Z")
    print("get\t\tpassed")
except:
    print("get\t\tfailed")

try:
    ht.remove("Z")
    print("remove\t\tpassed")
except:
    print("remove\t\tfailed")

print("---[Heap]---")
h = DSAHeap.DSAHeap(10)
try:
    if h.isEmpty() is False:
        raise ValueError
    print("isEmpty\t\tpassed")
except:
    print("isEmpty\t\tfailed")

try:
    if h.isFull() is True:
        raise ValueError
    print("isFull\t\tpassed")
except:
    print("isFull\t\tfaled")

try:
    h.insert(8, "a")
    h.insert(1, "b")
    print("insert\t\tpassed")
except:
    print("insert\t\tfailed")

try:
    p,v = h.remove()
    if p != 1 and v != "b":
        raise ValueError
    print("remove\t\tpassed")
except:
    print("remove\t\tfailed")

print("---[UAV]---")
u = DSAUav.UAV()
try:
    u.importFile("txtFiles/location.txt", "txtFiles/UAVdata.txt")
    print("importFile\tpassed")
except:
    print("importFile\tfailed")

try:
    u.travel("A", "G")
    print("travel\t\tpassed")
except:
    print("travel\t\tfailed")

try:
    u.DFS("A")
    print("DFS\t\tpassed")
except:
    print("DFS\t\tfailed")