# Graph Patterns

When you see a graph problem, first ask:

```text
1. Is the graph directed or undirected?
2. Is it weighted or unweighted?
3. Do I need to visit/explore nodes?
4. Do I need shortest path?
5. Do I need to detect cycles?
6. Do I need to group/connect components?
7. Do I need ordering/dependencies?
```

---

## 1. BFS

**Pattern:** Explore level by level.

```text
Queue
FIFO
```

Use when:

- Shortest path in an **unweighted** graph
- Minimum number of moves/steps
- Level-by-level exploration
- Multi-source spreading

```python
queue = deque([start])
visited = {start}

while queue:
    node = queue.popleft()

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
```

**Mental trigger:**

> "Minimum number of edges/steps?"

→ **BFS**

---

# 2. DFS

**Pattern:** Explore one path completely before exploring another.

```text
Stack / Recursion
LIFO
```

Use when:

- Exploring a graph
- Connected components
- Cycle detection
- Path exploration
- Backtracking
- Topological sort

```python
def dfs(node):
    if node in visited:
        return

    visited.add(node)

    for neighbor in graph[node]:
        dfs(neighbor)
```

**Mental trigger:**

> "I need to completely explore this structure/path."

→ **DFS**

---

# 3. Union Find / DSU

**Pattern:** Maintain groups of connected components.

Union Find is particularly useful when you repeatedly ask:

> "Are these two nodes connected?"

It maintains **sets/groups** of nodes.

```text
Initially:

A   B   C   D

Union(A, B)

AB   C   D

Union(B, C)

ABC   D
```

Two main operations:

```text
find(x)
→ Which group does x belong to?

union(a, b)
→ Merge the groups containing a and b.
```

Basic implementation:

```python
parent = list(range(n))

def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa == pb:
        return False

    parent[pb] = pa
    return True
```

### Use Union Find when:

- Need to connect components
- Need to determine whether two nodes are connected
- Detect cycles in an **undirected graph**
- Dynamic connectivity
- Minimum Spanning Tree → **Kruskal's algorithm**

### Mental trigger

> "Are these things in the same group?"

→ **Union Find**

---

# 4. Topological Sort

**Pattern:** Find an ordering where dependencies come first.

Example:

```text
A → B → C

A must happen before B
B must happen before C

Result:
A, B, C
```

Common use cases:

- Course prerequisites
- Build systems
- Task dependencies
- Package dependencies
- Scheduling

Works on a **DAG**:

```text
Directed Acyclic Graph
```

Two common approaches:

```text
Kahn's Algorithm → BFS + indegree

DFS → DFS + postorder
```

### Kahn's pattern

```python
indegree = [0] * n

for node in graph:
    for neighbor in graph[node]:
        indegree[neighbor] += 1

queue = deque(
    node for node in range(n)
    if indegree[node] == 0
)

while queue:
    node = queue.popleft()

    for neighbor in graph[node]:
        indegree[neighbor] -= 1

        if indegree[neighbor] == 0:
            queue.append(neighbor)
```

### Mental trigger

> "A must happen before B."

→ **Topological Sort**

---

# 5. Dijkstra

**Pattern:** Shortest path with **non-negative edge weights**.

```text
A --4-- B
|       |
2       1
|       |
C --3-- D
```

Use when:

> "What is the minimum cost/distance from A to B?"

Use a **min heap**.

```python
heap = [(0, start)]
dist = [float("inf")] * n
dist[start] = 0

while heap:
    distance, node = heapq.heappop(heap)

    if distance > dist[node]:
        continue

    for neighbor, weight in graph[node]:
        new_distance = distance + weight

        if new_distance < dist[neighbor]:
            dist[neighbor] = new_distance
            heapq.heappush(heap, (new_distance, neighbor))
```

### Mental trigger

> "Shortest/cheapest path + weighted graph?"

→ **Dijkstra**

**Important:** Dijkstra requires non-negative edge weights.

---

# 6. 0-1 BFS

Special case of shortest path where every edge has weight:

```text
0 or 1
```

Instead of a heap, use a **deque**.

```python
if weight == 0:
    deque.appendleft(neighbor)
else:
    deque.append(neighbor)
```

Why?

```text
0-cost edge → process sooner
1-cost edge → process later
```

### Mental trigger

> "Shortest path + edge weights are only 0/1?"

→ **0-1 BFS**

---

# 7. Bellman-Ford

**Pattern:** Shortest path where negative edge weights may exist.

```text
Dijkstra:
negative weights ❌

Bellman-Ford:
negative weights ✅
```

It can also detect **negative cycles**.

Basic idea:

```text
Relax every edge
N - 1 times
```

### Mental trigger

> "Shortest path + negative edges?"

→ **Bellman-Ford**

---

# 8. Minimum Spanning Tree

Different problem from shortest path.

You want to connect **all nodes** with minimum total edge cost.

Two major algorithms:

```text
Prim's
Kruskal's
```

### Prim's

Think:

> "Grow one connected tree."

Uses:

```text
Min Heap
```

### Kruskal's

Think:

> "Take the cheapest edges while avoiding cycles."

Uses:

```text
Sort edges
+
Union Find
```

### Mental trigger

> "Connect ALL nodes as cheaply as possible?"

→ **MST**

Not Dijkstra.

---

# 9. Cycle Detection

### Undirected Graph

Common approaches:

```text
DFS
Union Find
```

With Union Find:

```python
if find(a) == find(b):
    # cycle
```

Because if `a` and `b` are already in the same component, adding that edge creates a cycle.

---

### Directed Graph

Use:

```text
DFS + recursion state
```

or

```text
Topological Sort
```

A useful DFS state representation:

```text
0 → not visited
1 → currently visiting
2 → completely processed
```

If during DFS you reach a node with state `1`:

```text
cycle detected
```

---

# 10. Connected Components

**Pattern:** Find separate groups of connected nodes.

Example:

```text
A -- B       D -- E
     |
     C

Component 1: A B C
Component 2: D E
```

Use:

```text
DFS
BFS
Union Find
```

### Mental trigger

> "How many separate groups are there?"

→ **DFS / BFS / Union Find**

---

# 🧠 Graph Pattern Cheat Sheet

This is the part I'd memorize:

```text
GRAPH
│
├── Explore nodes
│   ├── BFS
│   └── DFS
│
├── Shortest path
│   ├── Unweighted      → BFS
│   ├── 0/1 weights     → 0-1 BFS
│   ├── Positive weights → Dijkstra
│   └── Negative weights → Bellman-Ford
│
├── Connected groups
│   ├── DFS
│   ├── BFS
│   └── Union Find
│
├── Dependencies / ordering
│   └── Topological Sort
│
├── Cycle detection
│   ├── Undirected → DFS / Union Find
│   └── Directed   → DFS / Topological Sort
│
└── Connect everything cheaply
    └── Minimum Spanning Tree
        ├── Prim's
        └── Kruskal's + Union Find
```

### The biggest distinctions to remember

```text
BFS
→ shortest PATH in unweighted graph

Dijkstra
→ shortest PATH in weighted graph

Union Find
→ connected COMPONENTS / grouping

Topological Sort
→ dependency ORDERING

MST
→ connect ALL nodes with minimum total COST
```

That last distinction—**shortest path vs. minimum spanning tree**—is especially important. They sound similar but solve fundamentally different problems.
