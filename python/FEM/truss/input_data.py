""" 
The purpose of this module is to initialize the necessary data 
for the FEM to start. 
"""
import numpy as np
from classes_used import Node, Elem

nele = 3 # num elements
nnodes = 3 # num of nodes
nne  = 2 # num of nodes per element
ndof = 2 # num of DOF of node
E    = 200000 # MPa
A    = 2300 # mm2

# Real DOF for the construction
rdof = np.array([[0,0],
    [1,0],
    [1,1]])

node1 = Node(0, 0, pins = (True, True), abs_pos = 0)
node2 = Node(4000, 0, pins = (False, True), load = (0, None), abs_pos = 1)
node3 = Node(4000, 6000, load = (12000, 0), abs_pos = 2)

elem1 = Elem(node1, node2, E = E, A = A)
elem2 = Elem(node2, node3, E = E, A = A)
elem3 = Elem(node1, node3, E = E, A = A)

elems = [elem1, elem2, elem3]
nodes = [node1, node2, node3]
