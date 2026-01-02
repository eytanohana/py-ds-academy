# Queue

A **Queue** is a First-In-First-Out (FIFO) data structure where elements are added at one end (rear) and removed from the other end (front).

## Overview

The Queue implementation in py-ds-academy is backed by a [linked list](linked-lists.md), providing O(1) enqueue and dequeue operations.

## Operations

### Creating a Queue

```python
from py_ds import Queue

# Create an empty queue
queue = Queue()

# Create a queue from an iterable
queue = Queue([1, 2, 3])
```

### Adding Elements

```python
# Enqueue an item at the rear
queue.enqueue(4)  # O(1)
```

### Removing Elements

```python
# Dequeue and return the front item
item = queue.dequeue()  # O(1), raises IndexError if empty
```

### Accessing Elements

```python
# Peek at the front without removing
front = queue.peek()  # O(1), raises IndexError if empty
```

### Utility Methods

```python
# Check if queue is empty
is_empty = queue.is_empty()  # O(1)

# Get the number of elements
length = len(queue)  # O(1)

# Clear all elements
queue.clear()  # O(1)

# Convert to list
items = list(queue)  # O(n)

# Extend with multiple items
queue.extend([5, 6, 7])  # O(k) where k is number of items
```

### Iteration

```python
# Iterate over queue (from front to rear)
for item in queue:
    print(item)

# Convert to list
items = list(queue)
```

## Time Complexity

| Operation       | Time Complexity |
|-----------------|-----------------|
| `enqueue(item)` | O(1)            |
| `dequeue()`     | O(1)            |
| `peek()`        | O(1)            |
| `is_empty()`    | O(1)            |
| `__len__()`     | O(1)            |
| `clear()`       | O(1)            |
| `__list__()`    | O(n)            |
| `extend(items)` | O(k)            |
| `__iter__()`    | O(n)            |

## Space Complexity

O(n) where n is the number of elements stored.

## Use Cases

- **Task Scheduling** - Processing tasks in order
- **Breadth-First Search** - Level-order tree/graph traversal
- **Buffering** - Managing data streams
- **Print Queue** - Managing print jobs
- **Message Queues** - Inter-process communication

## Example: Breadth-First Search

```python
def bfs_level_order(tree):
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
```

## Example: Task Scheduler

```python
class TaskScheduler:
    def __init__(self):
        self.queue = Queue()
    
    def add_task(self, task):
        self.queue.enqueue(task)
    
    def process_next(self):
        if not self.queue.is_empty():
            task = self.queue.dequeue()
            task.execute()
            return task
        return None
    
    def has_pending_tasks(self):
        return not self.queue.is_empty()
```
