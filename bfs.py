'''
Author   :    Hameed Abdul
Date     :    4/20/18
Purpose  :    Implement BFS from lecture
'''

import numpy as np
#import pandas as pd
import random


# Que datastructure for BFS
class que:
    def __init__(self):
        self.items = []

    def enque(self, newVal):
        self.items.insert(0, newVal)

    def deque(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def top(self):
        return self.items[-1]

# Numpy produces random DIRECTED graph
#graph_matrix = np.random.randint(0, 2, (6, 6))
graph_matrix = np.array([ [0,1,0,0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]])

# Pandas to help visualize data
# graph_plot = pd.DataFrame(graph_matrix)
# graph_plot

# Number of Vertices in the Graph
v = len(graph_matrix)

# Numpy Arrays to track distance from source and predessecer of node that led to arrival
dist = np.zeros(v)
pred = np.zeros(v)

# Numpy Boolean Array to track which nodes have been visited
visited = np.zeros(v, dtype=bool)

# Random vertex in our graph
source = random.randint(0, v-1)

def bfs(graph_matrix, source):
    '''
    :param graph_matrix: an n*n array that stores the edges between vertices
    :param source: vertex to begin traversal from
    :return: The distance, predeccessor and visistation of each vertex in relation to the source.
    '''

    # Change the distance, predecessor and vistitation status of the source vertex
    dist[source] = 0
    pred[source] = None
    visited[source] = True

    # Create a que and enque source
    quey = que()
    quey.enque(source)

    # While the que is not empty traverse the graph
    while not quey.isEmpty():
        # Grab the vertex at the top of the que
        # As well as all of that vertex's edges
        curr_node = quey.top()
        curr_edges = graph_matrix[curr_node]

        # For every edge
        for adj in range(0, v):
            # If a edge does exist and it has not already been visited
            if curr_edges[adj] == 1 and visited[adj] == False:
                # Set the distance, visitation and predeccessor information accordingly
                # Enque and continue
                dist[adj] = dist[curr_node] + 1
                pred[adj] = curr_node + 1
                visited[adj] = True
                quey.enque(adj)

        # Print status over time
        # Deque the current vertex
        print('Quey:', quey.items)
        quey.deque()

def test_bst():
    '''
    :return: Runs and validates my implementation of bst
    '''

    # Graph provided in handout
    graph_matrix = np.array([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]])
    bfs(graph_matrix, source)
    print('Graph:', graph_matrix)
    print('Dist:', dist)
    print('Pred:', pred)
    print('Visited', visited, '\n\n')

    # Numpy produces randomly generated graph
    graph_matrix = np.random.randint(0, 2, (6, 6))
    bfs(graph_matrix, source)
    print('Graph:', graph_matrix)
    print('Dist:', dist)
    print('Pred:', pred)
    print('Visited', visited, '\n\n')

test_bst()