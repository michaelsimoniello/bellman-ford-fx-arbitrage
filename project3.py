"""
Math 260
Bellman-Ford Arbitrage Final Project

Michael Simoniello
Date: 12/12/2024
"""

# Import math and p3tests
import math
from p3tests import *

################################################################################

"""
detectArbitrage
"""
def detectArbitrage(adjList, adjMat, tol=1e-15):
    """
    detectArbitrage- Detects arbitrage opportunities in a graph represented by
    adjacency list and matrix.

    Inputs:
        adjList (list of Vertex): Adjacency list representation of the graph.
        adjMat (list of list of floats): Adjacency matrix with edge weights
        as -log(exchange rate).
        tol (float): Tolerance value for floating-point precision.

    Output:
        list of int: A list of vertex ranks representing the negative cost
        cycle, or an empty list if none exists.
        """
    # Initialize the start vertex distance to 0 and all others to infinity
    for vertex in adjList:
        vertex.dist = float('inf')
        vertex.prev = None
    adjList[0].dist = 0

    # |V| - 1 iterations to determine the shortest path to each vertex
    # u represents the vertex and v represents its neighbors
    for i in range(len(adjList) - 1):
        for u in adjList:
            for v in u.neigh:
                weight = adjMat[u.rank][v.rank]
                if v.dist > u.dist + weight + tol: # Includes tolerance
                    v.dist = u.dist + weight
                    v.prev = u

    # Check for negative cost cycles by iterating one more time and checking
    # if there is still a shorter path
    changed_Vertex = None
    for u in adjList:
        for v in u.neigh:
            weight = adjMat[u.rank][v.rank]
            if v.dist > u.dist + weight + tol:  # Includes tolerance
                changed_Vertex = v
                break
        if changed_Vertex:
            break

    # Return empty list if no negative cost cycle is found
    if not changed_Vertex:
        return []

    # Initialize list to contain cycle/set to check which vertices were visited
    cycle = []
    visited = set()
    current = changed_Vertex

    # Detect cycle by visiting nodes repeatedly until same node is seen twice
    while current.rank not in visited:
        visited.add(current.rank)
        current = current.prev

    # The cycle starts and ends at same vertex
    start = current.rank

    # Trace the cycle path to construct the list named "cycle"
    while True:
        cycle.append(current.rank)
        current = current.prev
        if current.rank == start:
            cycle.append(start)
            break
    return cycle[::-1]  # Reverses the cycle to correct the order


"""
rates2mat
"""
def rates2mat(rates):
    """
       rates2mat- Converts exchange rates into a graph adjacency matrix with
       edge weights as negative logs.

       Input: rates (list of list of floats): Exchange rates matrix.

       Output: list of list of floats: Adjacency matrix with weights as -log(
       exchange rate).
           """
    return [[-math.log(R) for R in row] for row in rates]


"""
Main function.
"""
if __name__ == "__main__":
    testRates()
