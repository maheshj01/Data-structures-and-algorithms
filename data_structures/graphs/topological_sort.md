# Topological Sort

Topological Sort is a way of **ordering nodes in a directed graph when some nodes have to come before others**.

### Simple example

Imagine you have these tasks:

```text
Study → Exam
Study → Assignment
Assignment → Submit
```

This means:

```text
Study must happen before Exam
Study must happen before Assignment
Assignment must happen before Submit
```

A valid ordering is:

```text
Study → Exam → Assignment → Submit
```

Another valid ordering could be:

```text
Study → Assignment → Exam → Submit
```

The important thing is that **dependencies always come before the thing that depends on them**.

---

# When do we use it?

Topological Sort is useful when you see:

- Prerequisites
- Dependencies
- Tasks that must happen before other tasks
- Course scheduling
- Build/package dependencies
- Ordering jobs/tasks

### Mental trigger

> **"A must happen before B."**

Think:

**Topological Sort**

---

# Important: Directed Acyclic Graph

Topological sorting works on a:

```text
DAG
Directed Acyclic Graph
```

Meaning:

```text
Directed → edges have a direction

A → B
```

and:

```text
Acyclic → no cycle
```

A cycle like this:

```text
A → B → C
↑       ↓
└───────┘
```

has no valid ordering.

Why?

Because:

```text
A must come before B
B must come before C
C must come before A
```

Impossible.

---

# Kahn's Algorithm

One of the easiest ways to implement Topological Sort is **Kahn's Algorithm**.

It uses:

```text
Indegree + Queue + BFS
```

### What is indegree?

**Indegree = number of incoming edges.**

Example:

```text
A → B
A → C
B → C
```

Indegrees:

```text
A = 0
B = 1
C = 2
```

Visualize it as:

```text
A ─────→ B ─────→ C
 \                ↑
  └───────────────┘

A: 0 dependencies
B: 1 dependency
C: 2 dependencies
```

A node with:

```text
indegree = 0
```

has **nothing that needs to happen before it**, so we can process it.

---

# Simple Example

Let's use:

```text
A → C
B → C
C → D
```

### Step 1 — Calculate indegree

```text
A → C
B → C
C → D
```

Therefore:

```text
A = 0
B = 0
C = 2
D = 1
```

Put all `indegree == 0` nodes into the queue:

```text
Queue:
[A, B]
```

---

# Dry Run

### Step 1

Remove `A`:

```text
Queue:
[B]
```

Process its edge:

```text
A → C
```

Decrease C's indegree:

```text
C: 2 → 1
```

Result:

```text
Order: [A]

Indegree:
A = 0
B = 0
C = 1
D = 1
```

---

### Step 2

Remove `B`:

```text
Queue:
[]
```

Process:

```text
B → C
```

Decrease C:

```text
C: 1 → 0
```

C is now available.

Add it:

```text
Queue:
[C]
```

Order:

```text
[A, B]
```

---

### Step 3

Remove `C`:

```text
Queue:
[]
```

Process:

```text
C → D
```

Decrease D:

```text
D: 1 → 0
```

Add D:

```text
Queue:
[D]
```

Order:

```text
[A, B, C]
```

---

### Step 4

Remove `D`:

```text
Queue:
[]
```

D has no neighbors.

Final:

```text
[A, B, C, D]
```

This is a valid topological ordering.

---

# Code

```python
from collections import deque

def topological_sort(n, edges):
    graph = [[] for _ in range(n)]
    indegree = [0] * n

    for src, dst in edges:
        graph[src].append(dst)
        indegree[dst] += 1

    queue = deque()

    for node in range(n):
        if indegree[node] == 0:
            queue.append(node)

    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return result
```

---

# The Algorithm in Plain English

Remember these 5 steps:

```text
1. Build the graph
2. Calculate indegree for every node
3. Put all indegree-0 nodes into a queue
4. Remove nodes from queue and reduce their neighbors' indegree
5. Whenever a neighbor reaches 0, add it to the queue
```

Think of it like **unlocking tasks**:

```text
A has no prerequisites
        ↓
Do A
        ↓
A unlocks B
        ↓
Do B
        ↓
B unlocks C
        ↓
Do C
```

---

# How to Detect a Cycle

This is one of the most useful parts.

Suppose:

```text
A → B
B → C
C → A
```

Indegree:

```text
A = 1
B = 1
C = 1
```

There is **no node with indegree 0**.

Therefore:

```text
Queue = []
```

We can't start.

So there is a cycle.

More generally:

```python
if len(result) != n:
    # cycle exists
```

Because if there are `n` nodes but we could only process `n - 1`:

```text
Some node was blocked by a dependency
        ↓
That dependency was also blocked
        ↓
Eventually forms a cycle
```

---

# ⭐ Cheat Sheet

```text
TOPOLOGICAL SORT

Used for:
→ Dependencies
→ Prerequisites
→ Ordering tasks

Graph:
→ Directed
→ Usually DAG

Kahn's Algorithm:
→ BFS
→ Indegree
→ Queue

Process:
indegree 0
    ↓
queue
    ↓
process node
    ↓
decrease neighbors' indegree
    ↓
indegree becomes 0?
    ↓
add to queue

Cycle:
processed nodes < total nodes
        ↓
      cycle
```

### Most important mental model

> **A node becomes available when all of its prerequisites have been completed.**

That's essentially what `indegree == 0` represents.
