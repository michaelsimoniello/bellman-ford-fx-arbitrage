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
    ##### Your implementation goes here. #####
    return []
    ##### Your implementation goes here. #####

"""
rates2mat
"""
def rates2mat(rates):
    return [[-math.log(R) for R in row] for row in rates]


"""
Main function.
"""
if __name__ == "__main__":
    testRates()
