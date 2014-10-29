#!/usr/bin/env python

import sys
import os
FILE_DIR = os.path.dirname(__file__)
sys.path.append(os.path.join(FILE_DIR, '..'))

import pygraph.classes.graph
import pygraph.algorithms.minmax

class Node:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "node(" + str(self.value) + ")"

def problem81(matrix,graph,n_rows, n_cols):
    for r in xrange(n_rows):
        for c in xrange(n_cols):
            cur = matrix[r][c]
            # right
            if(c < n_cols - 1):
                right = matrix[r][c+1]
                graph.add_edge((cur, right), wt=right.value)
            # bottom, don't allow leftmost column to go down
            if(r < n_rows - 1 and c > 0):
                bottom = matrix[r+1][c]
                graph.add_edge((cur, bottom), wt=bottom.value)

    _, node_to_cost = pygraph.algorithms.minmax.shortest_path(graph, matrix[0][0])
    goal = matrix[n_rows - 1][n_cols - 1]
    print goal, node_to_cost[goal]

def problem82(matrix, graph,n_rows, n_cols):
    for r in xrange(n_rows):
        for c in xrange(n_cols):
            cur = matrix[r][c]
            # right
            if(c < n_cols - 1):
                right = matrix[r][c+1]
                graph.add_edge((cur, right), wt=right.value)
            # bottom, don't allow leftmost column to go down
            if(r < n_rows - 1 and c > 0):
                bottom = matrix[r+1][c]
                graph.add_edge((cur, bottom), wt=bottom.value)
            # top, don't allow leftmost column to go down
            if(r > 0 and c > 0):
                top = matrix[r-1][c]
                graph.add_edge((cur, top), wt=top.value)
    min_cost = 10e100
    for r in xrange(n_rows):
        print "row", r
        path, distances = pygraph.algorithms.minmax.shortest_path(graph, matrix[r][0])
        for r2 in xrange(n_rows):
            cur = matrix[r2][n_cols - 1]
            if cur in distances and distances[cur] < min_cost:
                min_cost = distances[cur]
                min_start = matrix[r][1]
                min_end = cur
                min_path = path
    print min_cost, min_start, min_end

def problem83(matrix,graph,n_rows, n_cols):
    for r in xrange(n_rows):
        for c in xrange(n_cols):
            cur = matrix[r][c]
            # right
            if(c < n_cols - 1):
                right = matrix[r][c+1]
                graph.add_edge((cur, right), wt=right.value)
            # bottom, don't allow leftmost column to go down
            if(r < n_rows - 1 and c > 0):
                bottom = matrix[r+1][c]
                graph.add_edge((cur, bottom), wt=bottom.value)
            # top, don't allow leftmost column to go down
            if(r > 0 and c > 0):
                top = matrix[r-1][c]
                graph.add_edge((cur, top), wt=top.value)
            # left
            if(c > 2):
                left = matrix[r][c-1]
                graph.add_edge((cur,left), wt=left.value)
    _, node_to_cost = pygraph.algorithms.minmax.shortest_path(graph, matrix[0][0])
    goal = matrix[n_rows - 1][n_cols - 1]
    print goal, node_to_cost[goal]

def main():
    matrix = []
    # input_file = "p081_matrix.txt"
    # input_file = "p082_matrix.txt"
    # input_file = "small.txt"
    input_file = "p083_matrix.txt"
    for line in open (input_file):
        # add a column to the left since edge weight = node value
        row = [Node(0)]
        for x in line.split(','):
            row.append(Node(int(x)))
        matrix.append(row)
    
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    graph = pygraph.classes.digraph.digraph()

    for r in xrange(n_rows):
        for c in xrange(n_cols):
            cur = matrix[r][c]
            graph.add_node(cur)

    problem83(matrix, graph, n_rows, n_cols)

if __name__ == '__main__':
    main()
