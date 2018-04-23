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
    :return: Prints the discovery, finish, predeccessor and visistation of each vertex in relation to the source.
    '''
    # Number of Vertices in the Graph
    # Numpy Arrays to track distance from source and predessecer of node that led to arrival
    # Numpy Boolean Array to track which nodes have been visited
    v = len(graph_matrix)
    disc = np.zeros(v, dtype=int)
    finish = np.zeros(v, dtype=int)
    pred = np.zeros(v)
    visited = np.zeros(v, dtype=bool)

    # Time counter for discovery and finish array
    # Stack to traverse graph
    time = 1
    s = stack()

    # Begin travesal at the first vertex in the graph
    # Store the time and Predecessor
    # Push to stack and begin looking at adjacent vertices
    disc[0] = time
    time = time + 1
    pred[0] = np.nan
    s.push(0)

    while not s.isEmpty():
        # Grab the current vertex and it's edges from the stack
        curr_vertex = s.top()
        curr_edges = graph_matrix[curr_vertex]

        # Process if not already visited
        if visited[curr_vertex] == False:
            visited[curr_vertex] = True

            # Touch every edges of that belongs to the current vertex
            for i in range(0, v):
                # If the edge exist and has not already been visited push to stack
                if curr_edges[i] == 1:
                    if visited[i] == False:

                        # Store discovery time and predecessor
                        disc[i] = time
                        time = time + 1
                        pred[i] = curr_vertex

                        # Push to the stack and set to current vertex
                        # Move on and check the current edges vertex
                        s.push(i)
                        curr_vertex = s.top()
                        curr_edges = graph_matrix[curr_vertex]
                        visited[i] = True
        # Once we travese as deep as possible
        # Check the stack
        # Store finish time and pop the vertex from the stack
        curr_vertex = s.top()
        finish[curr_vertex] = time
        time = time + 1
        s.pop()

        # All remaining vertices that weren't traversed to
        untouched = np.where(visited == False)

        # If the stack is empty and there are unvisited vertices
        # Add them to the stack and process them
        if len(visited[untouched]) > 0 and s.isEmpty():
            # Grab the vertex
            # Store the discover and predecessor (assume that it has none)
            index = untouched[0][0]
            disc[index] = time
            time = time + 1
            pred[index] = np.nan

            # Check to see if the vertex has a predecessor
            # If so store it
            touched = np.where(visited == True)
            for x in np.nditer(touched):
                if graph_matrix[x][index] == 1:
                    pred[index] = x
            # Push to stack
            s.push(index)

    # Print Results
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

    # Random 6*6 graph
    graph_matrix = np.random.randint(0, 2, (6, 6))
    dfs(graph_matrix)

test_dfs()

