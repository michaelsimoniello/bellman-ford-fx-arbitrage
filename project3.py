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
    ##### Your implementation goes here. #####
    return []
    ##### Your implementation goes here. #####

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
