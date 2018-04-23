'''
Author   :    Hameed Abdul
Date     :    4/20/18
Purpose  :    Implement DFS from lecture
'''

import numpy as np
import pandas as pd
import random

# Stack datastructure for BFS
class stack:
    def __init__(self):
        self.items = []

    def push(self, newVal):
        self.items.append(newVal)

    def pop(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def top(self):
        return self.items[-1]

def dfs(graph_matrix):
    '''
    :param graph: n*n graph contain edges between each vertex
    :return: The discovery, finish, predeccessor and visistation of each vertex in relation to the source.
    '''
    # Number of Vertices in the Graph
    # Numpy Arrays to track distance from source and predessecer of node that led to arrival
    # Numpy Boolean Array to track which nodes have been visited
    v = len(graph_matrix)
    disc = np.zeros(v, dtype=int)
    finish = np.zeros(v, dtype=int)
    pred = np.zeros(v)
    visited = np.zeros(v, dtype=bool)

    time = 1
    s = stack()

    disc[0] = time
    time = time + 1

    pred[0] = np.nan
    s.push(0)

    while not s.isEmpty():
        curr_vertex = s.top()
        curr_edges = graph_matrix[curr_vertex]

        if visited[curr_vertex] == False:
            visited[curr_vertex] = True

            for i in range(0, v):
                if curr_edges[i] == 1:
                    if visited[i] == False:

                        disc[i] = time
                        time = time + 1

                        pred[i] = curr_vertex

                        s.push(i)
                        curr_vertex = s.top()
                        curr_edges = graph_matrix[curr_vertex]
                        visited[i] = True

        curr_vertex = s.top()
        finish[curr_vertex] = time
        time = time + 1
        s.pop()

        untouched = np.where(visited == False)

        if len(visited[untouched]) > 0 and s.isEmpty():
            index = untouched[0][0]
            disc[index] = time
            time = time + 1

            touched = np.where(visited == True)

            pred[index] = np.nan

            for x in np.nditer(touched):
                if graph_matrix[x][index] == 1:
                    pred[index] = x
            s.push(index)

    print('Graph \n=======================\n', graph_matrix)
    print('Disc:', disc)
    print('Finish:', finish)
    print('Pred:', pred)
    print('Visited', visited, '\n\n')

def test_dfs():
    '''
    :return: Runs and validates my implementation of dfs
    '''

    # Graph provided in handout
    graph_matrix = np.array([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]])
    dfs(graph_matrix)

    graph_matrix = np.random.randint(0, 2, (6, 6))
    dfs(graph_matrix)


test_dfs()

