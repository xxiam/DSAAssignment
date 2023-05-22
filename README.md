# DSAAssignment

## Problem Description: 

In this problem, you need to monitor bushfires using unmanned aerial vehicles (UAVs). The UAVs will
fly over an area of interest and collect data on temperature, humidity, wind speed, and other relevant
factors. The data collected by the UAVs needs to be processed to identify areas where there is a high
risk of bushfires and areas that need attention.

## User Guide:

---

`python3 DSAAssignment.py [option]`

the main program of the assignment

`-i` : interactive mode, the user controls the UAV

`-q` : a quick test to check if all methods are working, the file will run `quickTest()` only

---

`python3 scalabilityProgam.py`

opens the scalability program, a CLI program for the user to create custom locations, vertices, edges and the ability to remove existing locations with import and export of .txt files

---

## Description of Classes:

### From DSAGraph.py:
 - Graph
 - GraphVertex

### From DSAhash.py
 - DSAHashTable 
 - DSAHashEntry

### From DSAHeap.py
 - DSAHeap
 - DSAHeapEntry

### From DSALinkedList.py
 - DSALinkedList
 - DSALinkedListNode

### From DSAUav.py
 - UAV