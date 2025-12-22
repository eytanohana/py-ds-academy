# Binary Tree

A **Binary Tree** is a hierarchical data structure where each node has at most two children, referred to as the left child and right child.

## Overview

The BinaryTree implementation in py-ds-academy provides a generic base class for binary tree structures, supporting multiple traversal methods and tree operations.

## Structure

Each node contains:
- `value` - The data stored in the node
- `left` - Reference to the left child (or None)
- `right` - Reference to the right child (or None)

## Traversals

Binary trees can be traversed in several ways:

### Preorder Traversal

Visit: **Root → Left → Right**

```python
from py_ds.datastructures.trees.base import BinaryTree

tree = BinaryTree()
# ... build tree ...

for node in tree.preorder():
    print(node.value)
```

### Inorder Traversal

Visit: **Left → Root → Right**

```python
for node in tree.inorder():
    print(node.value)
```

### Postorder Traversal

Visit: **Left → Right → Root**

```python
for node in tree.postorder():
    print(node.value)
```

### Level-Order Traversal (BFS)

Visit nodes level by level, left to right:

```python
for node in tree.level_order():
    print(node.value)
```

## Operations

### Tree Height

```python
height = tree.height()  # O(n)
```

### Tree Visualization

```python
print(tree)  # Pretty-prints the tree structure
```

## Time Complexity

| Operation | Time Complexity |
|-----------|----------------|
| `preorder()` | O(n) |
| `inorder()` | O(n) |
| `postorder()` | O(n) |
| `level_order()` | O(n) |
| `height()` | O(n) |

## Space Complexity

- Traversals: O(h) where h is the height of the tree
- Storage: O(n) where n is the number of nodes

## Use Cases

- **Expression Trees** - Representing mathematical expressions
- **Hierarchical Data** - File systems, organization charts
- **Decision Trees** - Machine learning and AI
- **Syntax Trees** - Compiler design
- **Base for Specialized Trees** - BST, AVL, etc.

## Example: Expression Tree

```python
# Represent: (3 + 4) * 2
#        *
#       / \
#      +   2
#     / \
#    3   4

from py_ds.datastructures.trees.base import BinaryTree, _BinaryNode

tree = BinaryTree()
tree.root = _BinaryNode('*')
tree.root.left = _BinaryNode('+')
tree.root.right = _BinaryNode(2)
tree.root.left.left = _BinaryNode(3)
tree.root.left.right = _BinaryNode(4)

# Evaluate using postorder traversal
def evaluate(node):
    if isinstance(node.value, (int, float)):
        return node.value
    
    left_val = evaluate(node.left)
    right_val = evaluate(node.right)
    
    if node.value == '+':
        return left_val + right_val
    elif node.value == '-':
        return left_val - right_val
    elif node.value == '*':
        return left_val * right_val
    elif node.value == '/':
        return left_val / right_val

result = evaluate(tree.root)  # 14
```

## Example: Tree Height Calculation

```python
def max_depth(node):
    if node is None:
        return 0
    return 1 + max(max_depth(node.left), max_depth(node.right))

height = max_depth(tree.root)
```
