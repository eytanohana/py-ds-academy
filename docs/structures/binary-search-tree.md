# Binary Search Tree

A **Binary Search Tree (BST)** is a binary tree with the ordering property: for any node, all values in the left subtree are less than the node's value, and all values in the right subtree are greater than the node's value.

## Overview

The BinarySearchTree implementation extends BinaryTree and provides efficient search, insert, and delete operations with average O(log n) time complexity.

## Properties

- **Ordering Property**: `left < node < right` for all nodes
- **No Duplicates**: Each value appears at most once (implementation-dependent)
- **Inorder Traversal**: Produces sorted sequence

## Operations

### Creating a BST

```python
from py_ds import BinarySearchTree

# Create an empty BST
bst = BinarySearchTree()

# Create a BST from an iterable
bst = BinarySearchTree([5, 3, 7, 2, 4, 6, 8])

# Print the tree structure (visual representation)
print(bst)
# Output:
#      ┌── 8
#  ┌── 7
#  │   └── 6
#  5
#  │   ┌── 4
#  └── 3
#      └── 2
```

### Insertion

```python
# Insert a value
bst.insert(9)  # O(log n) average, O(n) worst case
```

### Search

```python
# Check if value exists
if 4 in bst:  # O(log n) average, O(n) worst case
    print("Found!")

# Or use contains method
if bst.contains(4):
    print("Found!")
```

### Deletion

```python
# Remove a value
bst.remove(3)  # O(log n) average, O(n) worst case
```

### Finding Min/Max

```python
# Find minimum value
min_val = bst.min()  # O(log n) average, O(n) worst case

# Find maximum value
max_val = bst.max()  # O(log n) average, O(n) worst case
```

### Traversals

All BinaryTree traversals are available:

```python
# Inorder (produces sorted sequence)
sorted_values = list(bst.inorder())

# Preorder
preorder_values = list(bst.preorder())

# Postorder
postorder_values = list(bst.postorder())

# Level-order (BFS)
level_order_values = list(bst.level_order())
```

## Time Complexity

| Operation | Average | Worst Case |
|-----------|---------|------------|
| `insert(item)` | O(log n) | O(n) |
| `remove(item)` | O(log n) | O(n) |
| `contains(item)` | O(log n) | O(n) |
| `min()` | O(log n) | O(n) |
| `max()` | O(log n) | O(n) |
| Traversals | O(n) | O(n) |

!!! note

    Worst case occurs when the tree becomes a linked list (unbalanced).

## Space Complexity

O(n) where n is the number of nodes.

## Use Cases

- **Sorted Data Storage** - Maintaining sorted order efficiently
- **Range Queries** - Finding all values in a range
- **Symbol Tables** - Key-value mappings
- **Priority Queues** - When combined with heap operations
- **Database Indexing** - B-trees are based on BST concepts

## Example: Sorted Data Storage

```python
bst = BinarySearchTree([5, 3, 7, 2, 4, 6, 8])

# Print the tree structure
print(bst)

# Get sorted values
sorted_data = list(bst.inorder())  # [2, 3, 4, 5, 6, 7, 8]

# Find values in range
def range_query(bst, low, high):
    result = []
    for value in bst.inorder():
        if low <= value <= high:
            result.append(value)
        elif value > high:
            break
    return result

values = range_query(bst, 3, 6)  # [3, 4, 5, 6]
```

## Example: Symbol Table

```python
class SymbolTable:
    def __init__(self):
        self.bst = BinarySearchTree()
        self.data = {}
    
    def put(self, key, value):
        self.bst.insert(key)
        self.data[key] = value
    
    def get(self, key):
        if key in self.bst:
            return self.data.get(key)
        return None
    
    def keys(self):
        return list(self.bst.inorder())
```

## Deletion Cases

The `remove` operation handles three cases:

1. **Node with no children** - Simply remove the node
2. **Node with one child** - Replace node with its child
3. **Node with two children** - Replace with inorder successor/predecessor

## Balancing

For guaranteed O(log n) performance, consider using [AVLTree](avl-tree.md) which automatically maintains balance.
