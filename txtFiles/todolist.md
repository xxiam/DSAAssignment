# tracking what to do and what I finsihed

## finished
- fix removeAt method in linkedList.py

- add value in DSAGraph.py, using UAVdata.py

- allow creation of new nodes and links

- every time the uav traverses a location, hash data into table

- compare and discuss efficiency of using hashtable instead of array

## to do:

- heap ( i dont know what im doing )
    - i dont know yet

- itinerary 
    - implement DFS search algorithm
        - hamiltonian cycle
    - create most efficient uav flight path

- writing and testing
    - yanno

## work in progress:
- fix BFS algorithm
    - work on the pathing list issue
        - the alg works, but the path still includes visited vertices that dont need to be in the path linkedList 
        - used dijkstra's algorithm but still needs to fix some datatypes:
            - change from dictionaries to hashTables

- create scalability program
    - create interactive menu and test functionality
        - working
    - allow deletion of nodes and links
        - DSAGraph.py:
            - work on removeNode and removeEdge
            - allow edit of weight
            - editVertex
    - create search method for finding nodes
        - use getVertex()

- DSAUav.py file
    - put all methods in and test functionality
        