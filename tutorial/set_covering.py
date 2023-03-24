""" 
Set Covering problem solution using Gurobipy.
---
Set covering consists in finding the least amount of subsets to cover a set. 
Each subset is defined with a max. radius.
"""

import gurobipy as gp
from gurobipy import GRB
import numpy as np
import os

# Define covering sets, i.e., nodes which cover node 'i'
# 'i' is the index of the element in the array
covering_sets = [
    [0, 1, 2, 3],       # Nodes covering node 0 - if I place the 'ambulance' in either of these, I can reach 0
    [1, 2],
    [2, 3],
    [3, 1]
]

m = gp.Model("set_covering")

# Add the variables to the model
X = m.addVars(
    len(covering_sets),
    vtype=GRB.BINARY,
    name="X"
)

## Define objective function:
# 'quicksum' is a fast (optimized) way to express summations in constraints/obj func.
expr = gp.quicksum(X[i] for i in range(len(covering_sets)))
m.setObjective(expr, GRB.MINIMIZE)

# Constraints:
for i in range(len(covering_sets)):
    m.addConstr(sum(X[j] for j in covering_sets[i]) >= 1, f"covering node [{i}]")

m.write('location.lp')

# Solve:
m.optimize()

for i in range(len(covering_sets)):
    print(f"X[{i}]: {X[i].X}")
