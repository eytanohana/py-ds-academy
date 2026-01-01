# Quick Start

Get started with py-ds-academy in minutes!

## Basic Usage

### Stack

A Last-In-First-Out (LIFO) data structure:

```python
from py_ds import Stack

# Create a stack
stack = Stack([1, 2, 3])

# Push an item
stack.push(4)

# Pop an item (removes and returns the last item)
item = stack.pop()  # Returns 4

# Peek at the top without removing
top = stack.peek()  # Returns 3

# Check if empty
is_empty = stack.is_empty()  # False

# Get length
length = len(stack)  # 3
```

### Queue

A First-In-First-Out (FIFO) data structure:

```python
from py_ds import Queue

# Create a queue
queue = Queue([1, 2, 3])

# Enqueue an item
queue.enqueue(4)

# Dequeue an item (removes and returns the first item)
item = queue.dequeue()  # Returns 1

# Peek at the front without removing
front = queue.peek()  # Returns 2

# Iterate over items
for item in queue:
    print(item)  # Prints 2, 3, 4
```

### Linked Lists

Dynamic data structures for efficient insertion and deletion:

```python
from py_ds import LinkedList, DoublyLinkedList

# Linked list
sll = LinkedList([1, 2, 3])
sll.append(4)  # O(1) operation
sll.prepend(0)  # O(1) operation
print(list(sll))  # [0, 1, 2, 3, 4]
print(sll)  # HEAD → 0 → 1 → 2 → 3 → 4 → TAIL

# Doubly linked list (supports reverse iteration / more efficient append/prepend)
dll = DoublyLinkedList([1, 2, 3])
dll.append(4)  # O(1) operation
dll.prepend(0)  # O(1) operation
print(list(dll))  # [0, 1, 2, 3, 4]
print(dll)  # HEAD ⇆ 0 ⇆ 1 ⇆ 2 ⇆ 3 ⇆ 4 ⇆ TAIL

# Reverse iteration (doubly linked only)
for item in dll.reverse_iter():
    print(item)  # Prints 4, 3, 2, 1, 0
```

### Heaps

Priority queue implementations:

```python
from py_ds import MinHeap, MaxHeap

# Min heap (smallest element at top)
min_heap = MinHeap([3, 1, 4, 1, 5])
min_heap.push(2)
smallest = min_heap.pop()  # Returns 1
print(min_heap.peek())  # Returns 1 (next smallest)

# Max heap (largest element at top)
max_heap = MaxHeap([3, 1, 4, 1, 5])
max_heap.push(10)
largest = max_heap.pop()  # Returns 10
print(max_heap.peek())  # Returns 5 (next largest)
```

### Binary Search Tree

Efficient searching and sorting:

```python
from py_ds import BinarySearchTree

# Create a BST
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

# Search for an element
if 4 in bst:
    print("Found!")

# Traverse in different orders
print(list(bst.inorder()))    # [2, 3, 4, 5, 6, 7, 8]
print(list(bst.preorder()))   # [5, 3, 2, 4, 7, 6, 8]
print(list(bst.postorder()))  # [2, 4, 3, 6, 8, 7, 5]
print(list(bst.level_order()))  # [5, 3, 7, 2, 4, 6, 8]

# Find min and max
print(bst.min())  # 2
print(bst.max())  # 8

# Remove an element
bst.remove(3)
```

### AVL Tree

Self-balancing binary search tree:

```python
from py_ds import AVLTree

# Create an AVL tree (automatically balances)
avl = AVLTree([1, 2, 3, 4, 5, 6, 7])

# Print the tree structure (visual representation)
print(avl)
# Output:
#      ┌── 7
#  ┌── 6
#  │   └── 5
#  4
#  │   ┌── 3
#  └── 2
#      └── 1

# All BST operations work, with guaranteed O(log n) performance
avl.insert(8)
avl.remove(4)

# Check if balanced
print(avl.height)  # Tree height is kept minimal
```

## Common Patterns

### Using Stacks for Expression Evaluation

```python
from py_ds import Stack


def evaluate_postfix(expression: str) -> tuple[str, int]:
    stack = Stack()
    expression_str = Stack()

    for token in expression.split():
        if token.isdigit():
            stack.push(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                stack.push(a // b)
            elif token == '^':
                stack.push(a ** b)
            else:
                raise Exception(f'unsupported operand {token}')

            if not expression_str:
                expression_str.push(f'({a} {token} {b})')
            else:
                a = expression_str.pop()
                expression_str.push(f'({a} {token} {b})')
    return expression_str.pop()[1:-1], stack.pop()


expression, result = evaluate_postfix("3 4 + 2 * 5 - 2 ^")  # (((3 + 4) * 2) - 5) ^ 2 = 81
print(f'{expression} = {result}')
```

### Using Queues for BFS

```python
from py_ds import Queue, BinarySearchTree


def bfs_level_order(tree: BinarySearchTree):
    if not tree.root:
        return []

    queue = Queue([tree.root])
    result = []

    while not queue.is_empty():
        node = queue.dequeue()
        result.append(node.value)

        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)

    return result

tree = BinarySearchTree[int]([5, 3, 4, 7])
#   ┌── 7
#   5
#   │   ┌── 4
#   └── 3

print(bfs_level_order(tree))  # [5, 3, 7, 4]
```

### Using Heaps for Top-K Elements

```python
def find_top_k(items, k):
    min_heap = MinHeap()
    
    for item in items:
        if len(min_heap) < k:
            min_heap.push(item)
        elif item > min_heap.peek():
            min_heap.pop()
            min_heap.push(item)
    
    return sorted(min_heap.to_list(), reverse=True)

top_3 = find_top_k([1, 5, 3, 9, 2, 7, 4, 8], 3)  # [9, 8, 7]
```

## Type Hints

All data structures support full type hints:

```python
from typing import List
from py_ds import Stack

def process_stack(items: List[int]) -> Stack[int]:
    stack = Stack(items)
    return stack
```

## Error Handling

Data structures raise appropriate exceptions:

```python
from py_ds import Stack, Queue

stack = Stack()
try:
    stack.pop()  # Raises IndexError
except IndexError:
    print("Stack is empty!")

queue = Queue()
try:
    queue.dequeue()  # Raises IndexError
except IndexError:
    print("Queue is empty!")
```

## Next Steps

- Explore detailed documentation for each [Data Structure](../structures/index.md)
- Check out the complete [API Reference](../reference/index.md)
- See [Installation Guide](installation.md) for setup instructions
