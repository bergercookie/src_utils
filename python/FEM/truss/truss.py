#!/opt/local/bin/python3.3
import numpy as np
from classes_used import Node, Elem
from general_functions import *
from input_data import nodes, elems, ndof, nele
from numpy.linalg import solve as axb_solve

# Parameter Configuration
np.set_printoptions(precision = 3)


# K-global matrix determination
kglob_total = np.zeros((ndof*nele, ndof*nele))
for one_elem in elems:
    #print("ELEMENT #{}".format(nc))
    #print(kglob_total, '\n'+'-'*70+'\n' )
    pos = (one_elem.node1.abs_pos*ndof, one_elem.node2.abs_pos*ndof)
    kglob_total[pos[0]:pos[0] + 2, pos[0]:pos[0] + 2] += one_elem.kglob[0:2,0:2] #upper left
    kglob_total[pos[1]:pos[1] + 2, pos[1]:pos[1] + 2] += one_elem.kglob[2:4,2:4] #lower right
    kglob_total[pos[0]:pos[0] + 2, pos[1]:pos[1] + 2] += one_elem.kglob[0:2,2:4] #upper right
    kglob_total[pos[1]:pos[1] + 2, pos[0]:pos[0] + 2] += one_elem.kglob[2:4,0:2] #lower left

print(np.round(kglob_total))

restrict_tot = 0
for node in nodes:
    restrict_tot += sum(i for i in node.pins)

kglob_min = np.zeros(restrict_tot ** 2)
F_min = np.zeros(restrict_tot)

#import ipdb; ipdb.set_trace() # BREAKPOINT
nc_K = 0
nc_F = 0
indexes_found = []
# Decide the cols which will be kept
for nc1, node1 in enumerate(nodes):
    for nc11, pin1 in enumerate(node1.pins):
        if not pin1:
            F_min[nc_F] = node1.load[nc11]
            nc_F += 1
            indexes_found.append((nc1, nc11)) #append the found node, position
            for nc2, node2 in enumerate(nodes):
                for nc22, pin2 in enumerate(node2.pins):
                    if not pin2:
                        kglob_min[nc_K] = kglob_total[nc1*ndof+nc11, nc2*ndof+nc22]
                        nc_K += 1

kglob_min = kglob_min.reshape((restrict_tot, restrict_tot))
print(np.round(kglob_min))
print(F_min)

# determine the deformations:
deformations = axb_solve(kglob_min, F_min)

# Assign the found deformations to the nodes
for nc, index_ in enumerate(indexes_found):
    print(index_)
    nodes[index_[0]].deforms[index_[1]] = deformations[nc]
print(nodes)
