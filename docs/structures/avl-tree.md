# AVL Tree

An **AVL Tree** (named after inventors Adelson-Velsky and Landis) is a self-balancing Binary Search Tree that maintains height balance through automatic rotations.

## Overview

The AVLTree implementation extends BinarySearchTree and guarantees O(log n) time complexity for all operations by maintaining the AVL property: the heights of the two child subtrees of any node differ by at most 1.

## Properties

- **AVL Property**: For every node, `|height(left) - height(right)| ≤ 1`
- **Balance Factor**: `balance_factor = height(left) - height(right)`
- **Automatic Rebalancing**: Tree rebalances after insertions and deletions
- **Guaranteed Performance**: O(log n) for all operations

## Operations

### Creating an AVL Tree

```python
from py_ds import AVLTree

# Create an empty AVL tree
avl = AVLTree()

# Create an AVL tree from an iterable
avl = AVLTree([1, 2, 3, 4, 5, 6, 7])
```

### Insertion

```python
# Insert a value (automatically rebalances)
avl.insert(8)  # O(log n)
```

### Deletion

```python
# Remove a value (automatically rebalances)
avl.remove(4)  # O(log n)
```

### Search

```python
# Check if value exists
if 5 in avl:  # O(log n)
    print("Found!")
```

### All BST Operations

All BinarySearchTree operations are available:

```python
# Min/Max
min_val = avl.min()  # O(log n)
max_val = avl.max()  # O(log n)

# Traversals
inorder = list(avl.inorder())
preorder = list(avl.preorder())
postorder = list(avl.postorder())
level_order = list(avl.level_order())
```

## Rotations

AVL trees use rotations to maintain balance:

### Left Rotation

Used when right subtree is taller:

```
    A              B
   / \            / \
  T1  B    ->    A   C
     / \        / \
    T2  C      T1 T2
```

### Right Rotation

Used when left subtree is taller:

```
      A          B
     / \        / \
    B   T3 ->  C   A
   / \        /   / \
  C   T2     T1  T2 T3
 /
T1
```

### Left-Right Rotation

Used for left-right imbalance:

```
    A            A              C
   / \          / \            / \
  B   T4  ->   C   T4   ->    B   A
 / \          / \            / \ / \
T1  C        B   T3        T1 T2 T3 T4
   / \      / \
  T2 T3    T1 T2
```

### Right-Left Rotation

Used for right-left imbalance:

```
  A            A              C
 / \          / \            / \
T1  B   ->   T1  C     ->   A   B
   / \          / \        / \ / \
  C   T4       T2  B      T1 T2 T3 T4
 / \              / \
T2 T3            T3 T4
```

## Time Complexity

| Operation | Time Complexity |
|-----------|----------------|
| `insert(item)` | O(log n) |
| `remove(item)` | O(log n) |
| `contains(item)` | O(log n) |
| `min()` | O(log n) |
| `max()` | O(log n) |
| Traversals | O(n) |

**All operations are guaranteed O(log n)** - no worst-case degradation to O(n).

## Space Complexity

O(n) where n is the number of nodes.

## Use Cases

- **When Guaranteed Performance Matters** - Critical applications requiring O(log n)
- **Real-Time Systems** - Predictable performance characteristics
- **Database Indexing** - When balanced trees are required
- **Priority Queues** - Combined with heap operations
- **Range Queries** - Efficient range searches on sorted data

## Example: Maintaining Sorted Order

```python
avl = AVLTree([5, 3, 7, 2, 4, 6, 8])

# Tree remains balanced after all operations
avl.insert(1)  # Automatically rebalances
avl.insert(9)  # Automatically rebalances
avl.remove(5)  # Automatically rebalances

# Height is kept minimal
print(avl.height())  # O(log n) height guaranteed

# All operations remain O(log n)
sorted_values = list(avl.inorder())  # Always sorted
```

## Example: Comparison with BST

```python
from py_ds import BinarySearchTree, AVLTree

# Worst case: inserting sorted sequence
values = list(range(1000))

# BST becomes a linked list (O(n) operations)
bst = BinarySearchTree(values)
print(bst.height())  # ~1000 (unbalanced!)

# AVL stays balanced (O(log n) operations)
avl = AVLTree(values)
print(avl.height())  # ~10 (balanced!)
```

## Balance Factor

Each node maintains a balance factor:

- `balance_factor = height(left) - height(right)`
- Valid values: -1, 0, or 1
- If balance factor is outside this range, rotation occurs

## When to Use AVL vs BST

**Use AVLTree when:**

- You need guaranteed O(log n) performance
- Data insertion order is unpredictable
- Worst-case performance matters
- You're inserting/deleting frequently

**Use BinarySearchTree when:**

- Data is inserted in random order
- Worst-case performance is acceptable
- Simplicity is preferred
- Memory overhead is a concern
