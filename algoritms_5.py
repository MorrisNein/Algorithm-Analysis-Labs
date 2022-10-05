# -*- coding: utf-8 -*-

import numpy as np
import igraph as ig
import cairocffi

"""# Data generation"""

g = ig.Graph.Erdos_Renyi(n=100, m=200)

ig.plot(g)

for i in range(5):
  print(g.get_adjacency()[i])

for i in range(10):
  print(i, ': ', g.get_adjlist()[i])

"""# Depth-first search"""

np.array(g.dfs(vid=1)[0])

for i in range(100):
  if i not in g.dfs(vid=1)[0]:
    print(i)

"""# Breadth-first search"""

g.get_shortest_paths(v=np.random.randint(low=0, high=100), to=np.random.randint(low=0, high=100))