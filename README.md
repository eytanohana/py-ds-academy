# py-ds

[![CI status](https://github.com/eytanohana/py-ds-academy/actions/workflows/ci.yml/badge.svg)](https://github.com/eytanohana/py-ds-academy/actions/workflows/ci.yml)

A small playground project for implementing classic data structures from scratch in Python.

The goal is **learning + correctness** (with tests), not squeezing out every last micro-optimization.

---

## 🧱 Project Goals

- Implement core data structures from scratch in Python
- Use type hints, clean APIs, and unit tests
- Compare different implementations (e.g., list-backed vs linked)
- Practice algorithmic reasoning & complexity analysis

---

## 📦 Project Layout

```text
py-ds/
├─ pyproject.toml
├─ README.md
├─ .python-version
├─ src/
│  └── py_ds/
│     ├── __init__.py
│     └── datastructures/
│        ├── __init__.py
│        ├── stack.py
│        ├── queue.py
│        ├── linked_list.py
│        ├── doubly_linked_list.py
│        ├── binary_tree.py
│        ├── bst.py
│        ├── heap.py
│        └── graph.py
└─ tests/
   ├─ test_stack.py
   ├─ test_queue.py
   └─ test_linked_list.py
```

All importable code lives under `src/py_ds/`.

---

## 🚀 Getting Started

Requires [uv](https://github.com/astral-sh/uv).

```bash
# create venv from .python-version
uv venv

# install dependencies (if any)
uv sync

# run tests
uv run pytest
```

You can also drop into a REPL:

```bash
uv run python
```

```python
>>> from py_ds.datastructures import Stack
>>> s = Stack([1, 2, 3])
>>> s.pop()
3
```

---

## 📚 Data Structures Roadmap

### 1. Linear Structures

**Stacks**
- [x] `Stack` backed by Python list
- [x] Operations: `push`, `pop`, `peek`, `is_empty`, `__len__`

**Queues**
- [x] `Queue` backed by python list
- [x] Operations: `enqueue`, `dequeue`, `peek`, `is_empty`, `__len__`

**Linked Lists**
- [ ] `SinglyLinkedList`
  - [ ] `append`, `prepend`, `insert`, `remove`, `find`
  - [ ] Iteration support (`__iter__`)
- [ ] `DoublyLinkedList`
  - [ ] Efficient insert/remove at both ends
  - [ ] Bidirectional traversal

---

### 2. Trees

**Binary Tree (generic node-based)**
- [ ] `BinaryTreeNode` (value, left, right)
- [ ] Traversals:
  - [ ] Preorder
  - [ ] Inorder
  - [ ] Postorder
  - [ ] Level-order (BFS)

**Binary Search Tree (BST)**
- [ ] Insert
- [ ] Search (`contains`, `find`)
- [ ] Delete (handle 0, 1, 2 children)
- [ ] Find min / max
- [ ] Inorder traversal (sorted output)

Later:
- [ ] Self-balancing tree (e.g., AVL or Red-Black) – optional stretch goal

---

### 3. Heaps / Priority Queues

**Binary Heap (min-heap or max-heap)**
- [ ] `insert`
- [ ] `peek`
- [ ] `extract`
- [ ] `heapify` from existing list
- [ ] Use cases: priority queue, heap sort

---

### 4. Hash-Based Structures

**Hash Map**
- [ ] Array of buckets
- [ ] Collision handling via chaining (linked lists) or open addressing
- [ ] Operations: `get`, `set`, `delete`, `__contains__`
- [ ] Basic resizing & load factor

**Hash Set**
- [ ] Built on top of `HashMap`
- [ ] Operations: `add`, `remove`, `contains`, iteration

---

### 5. Graphs

**Graph Representations**
- [ ] Adjacency list representation
- [ ] Optional: adjacency matrix

**Algorithms**
- [ ] BFS (breadth-first search)
- [ ] DFS (depth-first search)
- [ ] Path search (e.g. `has_path(u, v)`)

Stretch:
- [ ] Topological sort
- [ ] Dijkstra’s algorithm (weighted graphs)

---

## 🧪 Testing

Each data structure gets its own test module under `tests/`.

Run the whole suite:

```bash
uv run pytest
```

---

## 🧠 Design Principles

- Prefer **clear, readable code** over cleverness
- Use **type hints** everywhere
- Raise the right built-in exceptions
- Document time complexity in docstrings

---

## 📝 Future Ideas

- [ ] Benchmarks comparing implementations
- [ ] Tree / graph visualizations
- [ ] Jupyter notebooks for demos

---

This project is mainly for learning + fun. No guarantees — just data structures implemented by hand.
