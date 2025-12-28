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
from py_ds import BinarySearchTree

tree = BinarySearchTree([5, 3, 7, 2, 4])

for value in tree.preorder():
    print(value)  # 5, 3, 2, 4, 7
```

### Inorder Traversal

Visit: **Left → Root → Right**

```python
for value in tree.inorder():
    print(value)  # 2, 3, 4, 5, 7
```

### Postorder Traversal

Visit: **Left → Right → Root**

```python
for value in tree.postorder():
    print(value)  # 2, 4, 3, 7, 5
```

### Level-Order Traversal (BFS)

Visit nodes level by level, left to right:

```python
for value in tree.level_order():
    print(value)  # 5, 3, 7, 2, 4
```

## Operations

### Tree Height

```python
height = tree.height  # O(n)
```

### Tree Visualization

```python
from py_ds import BinarySearchTree

tree = BinarySearchTree([5, 3, 7, 2, 4])

# Print the tree structure (visual representation)
print(tree)
# Output:
#  ┌── 7
#  5
#  │   ┌── 4
#  └── 3
#      └── 2
```

## Time Complexity

| Operation | Time Complexity |
|-----------|----------------|
| `preorder()` | O(n) |
| `inorder()` | O(n) |
| `postorder()` | O(n) |
| `level_order()` | O(n) |
| `height` | O(n) |

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

# Create a simple concrete class for building expression trees
class ExpressionTree(BinaryTree):
    """A simple binary tree for building expression trees manually."""
    
    def insert(self, value):
        """Not used for expression trees - we build manually."""
        pass
    
    def remove(self, value):
        """Not used for expression trees."""
        pass

# Build the expression tree manually
tree = ExpressionTree()
tree._root = _BinaryNode('*')
tree._root.left = _BinaryNode('+')
tree._root.right = _BinaryNode(2)
tree._root.left.left = _BinaryNode(3)
tree._root.left.right = _BinaryNode(4)
tree.size = 5  # Update size manually

# Print the tree structure
print(tree)
# Output:
#  ┌── 2
#  *
#  │   ┌── 4
#  └── +
#      └── 3

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

result = evaluate(tree._root)  # 14
print(f"Result: {result}")  # Result: 14
```

## Example: Tree Traversal

```python
from py_ds import BinarySearchTree

# Create a binary search tree
tree = BinarySearchTree([5, 3, 7, 2, 4, 6, 8])

# Print the tree structure
print(tree)
# Output:
#      ┌── 8
#  ┌── 7
#  │   └── 6
#  5
#  │   ┌── 4
#  └── 3
#      └── 2

# Get tree height
print(tree.height)  # 2

# Traverse in different orders
print(list(tree.preorder()))   # [5, 3, 2, 4, 7, 6, 8]
print(list(tree.inorder()))    # [2, 3, 4, 5, 6, 7, 8]
print(list(tree.postorder()))  # [2, 4, 3, 6, 8, 7, 5]
print(list(tree.level_order())) # [5, 3, 7, 2, 4, 6, 8]
```
