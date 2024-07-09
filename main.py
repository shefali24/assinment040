
### 2. `main.py`

# ```python
"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""

def longest_path(graph: list) -> int:
    ord_top = topological_sort(graph)
    return calculate_longest_path(graph, ord_top)

# Helper function to perform topological sort
def topological_sort(graph):
    n = len(graph)
    inDeg = [0] * n
    for i in range(n):
        for j, _ in graph[i]:
            inDeg[j] += 1

    queue = []
    for i in range(n):
        if inDeg[i] == 0:
            queue.append(i)

    ord_top = []
    while queue:
        node = queue.pop(0)
        ord_top.append(node)
        for i, _ in graph[node]:
            inDeg[i] -= 1
            if inDeg[i] == 0:
                queue.append(i)

    return ord_top
# Function to calculate longest path using topological sort
def calculate_longest_path(graph, ord_top):
    n = len(graph)
    d = [-float('inf')] * n
    d[ord_top[0]] = 0

    for node in ord_top:
        for i, weight in graph[node]:
            if d[node] + weight > d[i]:
                d[i] = d[node] + weight

    return max(d)
'''
. for graph number 4 the output is coming out to be 2 instead of 3 .
. checked for self loops in this graph sepecifically here is the code:
def has_self_loop(graph):
  for node, i in enumerate(graph):
    if (node,) in i:
      return True  # Self-loop found

  return False  # No self-loops found

graph4 = [
  [(1, 1), (2, 1)],
  [(3, 1)],
  [(3, 1)],
  []
]

if has_self_loop(graph4):
  print("The graph contains at least one self-loop.")
else:
  print("The graph does not contain self-loops.")
'''

