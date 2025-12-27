# Data Structures Overview

This page provides an overview of all data structures implemented in py-ds-academy. Each structure includes detailed documentation, complexity analysis, and usage examples.

## 📊 Structure Categories

### Linear Structures

Linear data structures store elements in a sequential manner.

#### [Stack](stack.md)
A Last-In-First-Out (LIFO) data structure backed by a Python list.

**Key Operations:**
- `push(item)` - O(1)
- `pop()` - O(1)
- `peek()` - O(1)

**Use Cases:** Expression evaluation, undo/redo functionality, backtracking algorithms

#### [Queue](queue.md)
A First-In-First-Out (FIFO) data structure backed by a Python list.

**Key Operations:**
- `enqueue(item)` - O(1)
- `dequeue()` - O(1)
- `peek()` - O(1)

**Use Cases:** Task scheduling, breadth-first search, buffering

#### [Linked Lists](linked-lists.md)
Dynamic data structures that store elements in nodes connected by pointers.

**Types:**
- **LinkedList** - Nodes point to next only
- **DoublyLinkedList** - Nodes point to both next and previous

**Key Operations:**
- `append(item)` - O(1) for both (using tail pointer)
- `prepend(item)` - O(1) for both
- `insert(index, item)` - O(n)
- `remove(item)` - O(n)

**Use Cases:** Dynamic memory allocation, implementing other data structures

---

### Trees

Hierarchical data structures with nodes connected by edges.

#### [Binary Tree](binary-tree.md)
A tree where each node has at most two children.

**Traversals:**
- Preorder - O(n)
- Inorder - O(n)
- Postorder - O(n)
- Level-order (BFS) - O(n)

**Use Cases:** Expression trees, hierarchical data representation

#### [Binary Search Tree](binary-search-tree.md)
A binary tree with ordering property: left < node < right.

**Key Operations:**
- `insert(item)` - O(log n) average, O(n) worst
- `remove(item)` - O(log n) average, O(n) worst
- `search(item)` - O(log n) average, O(n) worst

**Use Cases:** Searching, sorting, range queries

#### [AVL Tree](avl-tree.md)
A self-balancing binary search tree that maintains height balance.

**Key Features:**
- Automatic rebalancing via rotations
- Guaranteed O(log n) operations
- Balance factor tracking

**Use Cases:** When guaranteed O(log n) performance is required

---

### Heaps

Complete binary trees that satisfy the heap property.

#### [Heaps](heaps.md)
Priority queue implementations using binary heaps.

**Types:**
- **MinHeap** - Parent ≤ children
- **MaxHeap** - Parent ≥ children

**Key Operations:**
- `push(item)` - O(log n)
- `pop()` - O(log n)
- `peek()` - O(1)

**Use Cases:** Priority queues, heap sort, scheduling algorithms

---

## 🔍 Complexity Comparison

| Structure | Insert | Delete | Search | Space |
|-----------|--------|--------|--------|-------|
| Stack | O(1) | O(1) | O(n) | O(n) |
| Queue | O(1) | O(1) | O(n) | O(n) |
| LinkedList | O(1)* | O(n) | O(n) | O(n) |
| DoublyLinkedList | O(1) | O(n) | O(n) | O(n) |
| BinarySearchTree | O(log n) | O(log n) | O(log n) | O(n) |
| AVLTree | O(log n) | O(log n) | O(log n) | O(n) |
| Heap | O(log n) | O(log n) | O(n) | O(n) |

*O(1) for append at tail, O(n) for insert at arbitrary position

## 🎯 Choosing the Right Structure

- **Need LIFO?** → Use a **Stack**
- **Need FIFO?** → Use a **Queue**
- **Need dynamic size with O(1) append?** → Use a **LinkedList** or **DoublyLinkedList** (both support O(1) append)
- **Need sorted data with fast search?** → Use a **BinarySearchTree**
- **Need guaranteed O(log n) performance?** → Use an **AVLTree**
- **Need priority-based access?** → Use a **Heap**

## 📖 Next Steps

- Explore individual data structure pages for detailed documentation
- Check out the [API Reference](../reference/index.md) for complete method signatures
- See [Getting Started](../getting-started/quickstart.md) for usage examples