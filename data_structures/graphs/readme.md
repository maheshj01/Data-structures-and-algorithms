# Graphs

A **graph** is a collection of **nodes (vertices)** connected by **edges**.

Graphs can be:

- **Directed** → `A → B`
- **Undirected** → `A ↔ B`
- **Weighted** → edges have a cost/distance
- **Unweighted** → edges have no cost

Common graph representations:

```text
Adjacency List:
A → [B, C]
B → [A, D]
C → [A]
D → [B]
```

---

# BFS — Breadth-First Search

BFS explores the graph **level by level**.

> Visit the current node → visit all of its neighbors → then visit their neighbors → continue.

Think:

```text
        A
      /   \
     B     C
    / \     \
   D   E     F

BFS: A → B → C → D → E → F
```

Use a **queue** because the first node added should be the first node processed (**FIFO**).

### General Structure

```python
from collections import deque

queue = deque([start])
visited = {start}

while queue:
    node = queue.popleft()

    for neighbor in node.neighbors:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
```

### BFS is useful for

- Shortest path in an **unweighted graph**
- Finding nodes at a certain distance
- Level-order traversal
- Finding connected components
- Multi-source problems

### Key idea

```text
QUEUE → First In, First Out

Start
 ↓
Neighbors
 ↓
Neighbors of neighbors
 ↓
...
```

---

# DFS — Depth-First Search

DFS explores **as deep as possible along one path**, then **backtracks** when it can't go further.

Think:

```text
        A
      /   \
     B     C
    / \
   D   E

DFS: A → B → D → E → C
```

Use either:

- **Recursion** → call stack
- **Stack** → explicit storage

### Recursive Structure

```python
visited = set()

def dfs(node):
    if node in visited:
        return

    visited.add(node)

    for neighbor in node.neighbors:
        dfs(neighbor)

dfs(start)
```

### Iterative Structure

```python
stack = [start]
visited = {start}

while stack:
    node = stack.pop()

    for neighbor in node.neighbors:
        if neighbor not in visited:
            visited.add(neighbor)
            stack.append(neighbor)
```

### DFS is useful for

- Exploring all paths
- Connected components
- Cycle detection
- Backtracking
- Topological sorting
- Detecting graph structure

### Key idea

```text
STACK → Last In, First Out

Start
 ↓
Go deep
 ↓
Go deeper
 ↓
Dead end
 ↓
Backtrack
 ↓
Try another path
```

---

# BFS vs DFS

|                            | BFS            | DFS                     |
| -------------------------- | -------------- | ----------------------- |
| Data structure             | Queue          | Stack / Recursion       |
| Strategy                   | Level by level | Go deep, then backtrack |
| Shortest path (unweighted) | ✅             | ❌                      |
| Backtracking               | ❌             | ✅                      |
| Cycle detection            | ✅             | ✅                      |
| Typical memory             | `O(V)`         | `O(V)`                  |
| Time                       | `O(V + E)`     | `O(V + E)`              |

### ⭐ Remember

```text
BFS → Queue → Level by level → Shortest unweighted path

DFS → Stack → Go deep → Backtrack
```

And for **weighted graphs**, don't automatically reach for BFS/DFS. If edge weights matter, that's where algorithms like **Dijkstra**, **0-1 BFS**, or **Bellman-Ford** come in.

---

> To understand how to solve a graph problem see [patterns.md](./patterns.md)
