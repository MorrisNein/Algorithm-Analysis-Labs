# -*- coding: utf-8 -*-

import networkx as nx
import numpy as np
import time
import matplotlib.pyplot as plt

"""#Data generation"""

n = 100
m = 500

g = nx.gnm_random_graph(n, m)
weights = np.random.randint(100, size=m)

weights_matrix = np.zeros((m, m))

for i, elem in enumerate(g.edges()):
    g[elem[0]][elem[1]]['weight'] = weights[i]
    g[elem[1]][elem[0]]['weight'] = weights[i]
nx.draw(g)

vertice = np.random.randint(100)

"""#Path finding by Dijksrta algorithm"""

time_list_dijkstra = []
for i in range(10):
    start_time = time.time()
    path = nx.algorithms.shortest_paths.weighted.dijkstra_path(g, vertice, np.random.randint(100))
    iter_time = time.time() - start_time
    print(path)
    time_list_dijkstra.append(iter_time)
    print(i, ': ', iter_time)
print('Mean iter time:', np.mean(time_list_dijkstra))

"""#Path finding by Bellman-Ford algorithm"""

time_list_bf = []
for i in range(10):
    start_time = time.time()
    path = nx.algorithms.shortest_paths.weighted.bellman_ford_path(g, vertice, np.random.randint(100))
    iter_time = time.time() - start_time
    print(path)
    time_list_bf.append(iter_time)
    print(i, ': ', iter_time)
print('Mean iter time:', np.mean(time_list_bf))

"""#A* path finding"""

a_star_graph = nx.grid_2d_graph(10, 20)

nodes_to_del = []
to_del = np.random.choice(range(200), 40, replace=False)
for el in to_del:
  nodes_to_del.append(list(a_star_graph.nodes)[el])

a_star_graph.remove_nodes_from(nodes_to_del)

start, stop = list(a_star_graph.nodes)[np.random.randint(160)], list(a_star_graph.nodes)[np.random.randint(160)]
path = nx.algorithms.shortest_paths.astar.astar_path(a_star_graph, start, stop)

time_list_a = []

plt.figure(figsize=(10, 10))
pos = dict((n, n) for n in a_star_graph.nodes())
labels = dict(((i, j), i * 10 + j) for i, j in a_star_graph.nodes())
nx.draw_networkx(a_star_graph, pos=pos, labels=labels)
start, stop = list(a_star_graph.nodes)[np.random.randint(160)], list(a_star_graph.nodes)[np.random.randint(160)]
start_time = time.time()
path = nx.algorithms.shortest_paths.astar.astar_path(a_star_graph, start, stop)
time_list_a.append(time.time() - start_time)
print(path)
nx.draw_networkx_nodes(a_star_graph, pos, nodelist=path, node_color='r')

time_list_a = []
n = 5

fig = plt.figure(figsize=(20, 20))

for i in range(n):
    subplot = 331 + i
    start, stop = list(a_star_graph.nodes)[np.random.randint(160)], list(a_star_graph.nodes)[np.random.randint(160)]
    print(f'path from {start} to {stop}:')
    start_time = time.time()
    path = nx.algorithms.shortest_paths.astar.astar_path(
        a_star_graph, start, stop)
    time_list_a.append(time.time() - start_time)
    print(i, 'iter time:', time_list_a[i])
    ax = fig.add_subplot(subplot)
    nx.draw_networkx(a_star_graph, pos=pos, labels=labels)
    nx.draw_networkx_nodes(a_star_graph, pos, nodelist=path, node_color='r')
    print(path)
print('Mean iter time:', np.mean(time_list_a))
