# py-ds-academy

[![PyPI - Version](https://img.shields.io/pypi/v/py-ds-academy)](https://pypi.org/project/py-ds-academy/)
[![PyPI - License](https://img.shields.io/pypi/l/py-ds-academy)](https://github.com/eytanohana/py-ds-academy?tab=MIT-1-ov-file)
[![CI status](https://github.com/eytanohana/py-ds-academy/actions/workflows/ci.yml/badge.svg)](https://github.com/eytanohana/py-ds-academy/actions/workflows/ci.yml)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/py-ds-academy)](https://pypi.org/project/py-ds-academy/)

A small playground project for implementing classic data structures from scratch in Python.

## 📖 Documentation & Installation

- **📚 Documentation**: [View on GitHub Pages](https://eytanohana.github.io/py-ds-academy/)
- **📦 PyPI Package**: [Install from PyPI](https://pypi.org/project/py-ds-academy/)

```bash
pip install py-ds-academy
```

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
py-ds-academy/
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
│        ├── heaps.py
│        ├── linked_lists/
│        │  ├── __init__.py
│        │  ├── singly_linked.py
│        │  └── doubly_linked.py
│        └── trees/
│           ├── __init__.py
│           ├── base.py
│           ├── binary_search_tree.py
│           └── avl.py
└─ tests/
   ├─ test_stack.py
   ├─ test_queue.py
   ├─ test_linked_list.py
   ├─ test_doubly_linked_list.py
   ├─ test_max_heap.py
   ├─ test_min_heap.py
   ├─ test_binary_search_tree.py
   └─ test_avl_tree.py
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
>>> from py_ds import Stack, Queue, LinkedList, DoublyLinkedList
>>> from py_ds import MinHeap, MaxHeap, BinarySearchTree, AVLTree

>>> # Stack example
>>> s = Stack([1, 2, 3])
>>> s.pop()
3

>>> # Queue example
>>> q = Queue([1, 2, 3])
>>> q.dequeue()
1

>>> # Linked List example
>>> ll = LinkedList([1, 2, 3])
>>> ll.append(4)
>>> list(ll)
[1, 2, 3, 4]

>>> # Heap example
>>> h = MinHeap([3, 1, 4, 1, 5])
>>> h.pop()
1

>>> # BST example
>>> bst = BinarySearchTree([5, 3, 7, 2, 4])
>>> list(bst.inorder())
[2, 3, 4, 5, 7]
```

---

## 📚 Data Structures Roadmap

### 1. Linear Structures

**Stacks** ✅
- [x] `Stack` backed by Python list
- [x] Operations: `push`, `pop`, `peek`, `is_empty`, `__len__`, `clear`, `extend`, `to_list`
- [x] Iteration support (`__iter__`)

**Queues** ✅
- [x] `Queue` backed by Python list
- [x] Operations: `enqueue`, `dequeue`, `peek`, `is_empty`, `__len__`, `clear`, `extend`, `to_list`
- [x] Iteration support (`__iter__`)

**Linked Lists** ✅
- [x] `LinkedList`
  - [x] `append`, `prepend`, `insert`, `remove`, `pop`, `find`
  - [x] Iteration support (`__iter__`)
  - [x] Indexing support (`__getitem__`, `__setitem__`)
  - [x] `head()`, `tail()`, `clear()`
- [x] `DoublyLinkedList`
  - [x] Efficient O(1) `append` and `prepend` (with tail pointer)
  - [x] Bidirectional traversal (`__iter__`, `reverse_iter`)
  - [x] All operations from `LinkedList`
  - [x] Optimized indexing with bidirectional search

---

### 2. Trees

**Binary Tree (generic node-based)** ✅
- [x] `BinaryTree` base class with `_BinaryNode`
- [x] Traversals:
  - [x] Preorder (`preorder()`)
  - [x] Inorder (`inorder()`)
  - [x] Postorder (`postorder()`)
  - [x] Level-order / BFS (`level_order()`)
- [x] Tree height calculation
- [x] Tree visualization (`__str__`)

**Binary Search Tree (BST)** ✅
- [x] `BinarySearchTree` implementation
- [x] Insert
- [x] Search (`__contains__`)
- [x] Delete (`remove`) - handles 0, 1, 2 children
- [x] Find min / max (`min()`, `max()`)
- [x] Inherits all traversals from `BinaryTree`

**Self-Balancing Trees** ✅
- [x] `AVLTree` - self-balancing BST
  - [x] Automatic rebalancing on insert/remove
  - [x] Rotations: left, right, left-right, right-left
  - [x] Balance factor calculation
  - [x] Inherits all BST operations

---

### 3. Heaps / Priority Queues ✅

**Binary Heap**
- [x] `Heap` abstract base class
- [x] `MinHeap` implementation
- [x] `MaxHeap` implementation
- [x] Operations: `push`, `pop`, `peek`
- [x] Heap construction from iterable
- [x] `heapify_up` and `heapify_down` operations
- [x] Use cases: priority queue, heap sort

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

## ✨ Implemented Features Summary

The following data structures are fully implemented and tested:

- ✅ **Stack** - LIFO stack with list backing
- ✅ **Queue** - FIFO queue with list backing  
- ✅ **LinkedList** - Single-direction linked list
- ✅ **DoublyLinkedList** - Double-direction linked list with O(1) append/prepend
- ✅ **MinHeap** - Minimum binary heap
- ✅ **MaxHeap** - Maximum binary heap
- ✅ **BinarySearchTree** - Binary search tree with insert, remove, search, min/max
- ✅ **AVLTree** - Self-balancing AVL tree (extends BST)

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
- 
---

This project is mainly for learning + fun. No guarantees — just data structures implemented by hand.
