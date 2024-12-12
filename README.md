Arbitrage Final Project- Michael Simoniello
Date: 12/12/2024

Description: This project detects arbitrage opportunities in currency exchange rates using the Bellman-Ford algorithm. 
By converting exchange rates into a graph representation, the algorithm identifies negative cost cycles which correspond to arbitrage opportunities.


Background:
Currency arbitrage occurs when a sequence of currency exchanges results in a net profit. In financial markets, such opportunities are quickly eliminated as traders exploit them.
This project simulates detecting these fleeting opportunities by representing exchange rates as a weighted, directed graph and applying a shortest-path algorithm.


Features: 

What this project does-  detects arbitrage opportunities in currency exchange rates by representing them as a graph, where vertices are currencies and edges are exchange rates with weights as negative logarithms. 
First, it uses the Bellman-Ford algorithm to find negative weight cycles in the graph, which indicate arbitrage opportunities. 
If a cycle is found, the program traces the cycle to show the sequence of exchanges for profit. When calling testrates, the program outputs the results for each of the four test cases in p3tests, and when working properly,
it should pass all four tests.
 
Graph Representation Method - rates2mat

Exchange rates are transformed into a graph where vertices represent currencies, and edges represent exchange rates.
Edge weights are calculated as the negative logarithm of exchange rates to convert multiplicative relationships into additive ones.

Bellman-Ford Algorithm - detectArbitrage

The Bellman-Ford algorithm is used to detect negative weight cycles in the graph because a negative weight cycle indicates an arbitrage opportunity.
Set all distances to infinity, except for the start vertex (set to 0) and initialize prev pointers to None. 
Iterate ∣V∣−1 times, updating distances and previous pointers based on edge weights.
Include the tol value when comparing potential updates to account for small errors.
Perform an additional iteration to check for updates. If updates occur, trace the prev pointers to find the cycle.
Remove vertices not part of the cycle. Reverse the cycle (since tracing is backward) for proper ordering.

Vertex class - represents each currency as a graph vertex. 
It stores attributes like rank (unique identifier), neigh (list of neighboring vertices), dist (current shortest distance from the source), and prev (pointer to the previous vertex in the shortest path). 
These attributes are essential for traversing the graph and reconstructing cycles during the Bellman-Ford algorithm.

Currencies class - builds the graph of exchange rates by creating vertices (using the Vertex class) and organizing them into an adjacency list (adjList) and adjacency matrix (adjMat).
It provides methods to compute the adjacency matrix (rates2mat), detect arbitrage cycles (detectArbitrage), and print or verify results, serving as the primary interface for running the project.

Handling Precision Issues:

A tolerance value (tol) is used to address floating-point precision limitations when performing calculations, ensuring numerical stability.


Usage:

First, download the main file (project3.py) and the three provided files (p3tests, p3currencies, and p3vertex) to your computer. Run the program by calling the testRates function in the main block of the project3.py file (should already be there). The other files (p3tests, p3currencies, and p3vertex) can be left alone. 
However, if you want to custimize the input (i.e. to use more recent exchange rate data) modify the test cases in p3tests. Always run the code in the main file.


Testing: 4 cases and Expected OUTPUTS

1. Small Arbitrage Example (Exchange Rates 0)
Description: This test case uses a small set of 4 currencies with exchange rates manually set to create an arbitrage opportunity.

Expected Output: The program detects a negative cost cycle and identifies the correct arbitrage cycle(Euro,
Lira,
Dollar,
Euro) with the expected profit (For gain of: 0.020998 Euros). This verifies that the algorithm correctly handles small, controlled input data.

2. Real-World Exchange Rates (Exchange Rates 1)
Description: A real-world dataset with exchange rates between 14 currencies, where no arbitrage opportunities exist.
Example: Rates include 
USD, 
EUR, 
JPY, etc., based on actual market data.

Expected Output: The program should report that no negative cost cycle is found. This confirms the algorithm works correctly when no arbitrage opportunities exist.

3. Underpriced USD (Exchange Rates 2)
Description: A modified version of the real-world dataset where the USD is deliberately underpriced relative to the British Pound.
Example: The rate 
USD
→
GBP
USD→GBP is artificially adjusted to introduce an arbitrage opportunity.

Expected Output: The program detects the negative cost cycle corresponding to this contrived arbitrage (USD,
AUD,
GBP,
USD). Expected profit: (For gain of: 0.013019 USDs) This ensures the algorithm can identify specific, introduced arbitrage opportunities in large datasets.

4. Multiple Adjustments (Exchange Rates 3)
Description: Another modified dataset where multiple currencies (e.g., USD, JPY, and SAR) are either underpriced or overpriced relative to others.
Example: Adjustments create multiple potential arbitrage cycles, increasing complexity.

Expected Output: The program detects at least one valid negative cost cycle, (HKD
JPY,
INR,
SAR,
HKD)  Expected profit: (For gain of: 0.049645 HKDs), demonstrating robustness in handling more complex graphs with multiple cycles.

Note: The function logRates that was detailed in the code plan was left out because its goal is accomplished by rates2mat.
