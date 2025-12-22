# Heaps

A **Heap** is a complete binary tree that satisfies the heap property. Heaps are commonly used to implement priority queues.

## Overview

py-ds-academy provides two heap implementations:

- **MinHeap** - Parent nodes are always less than or equal to their children
- **MaxHeap** - Parent nodes are always greater than or equal to their children

## Heap Property

### MinHeap Property
For every node `i` (except root):
- `parent(i) ≤ node(i)`
- Smallest element is always at the root

### MaxHeap Property
For every node `i` (except root):
- `parent(i) ≥ node(i)`
- Largest element is always at the root

## Operations

### Creating a Heap

```python
from py_ds import MinHeap, MaxHeap

# Create an empty heap
min_heap = MinHeap()
max_heap = MaxHeap()

# Create a heap from an iterable
min_heap = MinHeap([3, 1, 4, 1, 5])
max_heap = MaxHeap([3, 1, 4, 1, 5])
```

### Adding Elements

```python
# Push an item onto the heap
min_heap.push(2)  # O(log n)
max_heap.push(10)  # O(log n)
```

### Removing Elements

```python
# Pop and return the root (min for MinHeap, max for MaxHeap)
min_item = min_heap.pop()  # O(log n)
max_item = max_heap.pop()  # O(log n)
```

### Accessing Elements

```python
# Peek at the root without removing
min_val = min_heap.peek()  # O(1)
max_val = max_heap.peek()  # O(1)
```

### Utility Methods

```python
# Check if heap is empty
is_empty = min_heap.is_empty()  # O(1)

# Get the number of elements
length = len(min_heap)  # O(1)

# Convert to list (not sorted!)
items = min_heap.to_list()  # O(n)
```

## Time Complexity

| Operation | Time Complexity |
|-----------|----------------|
| `push(item)` | O(log n) |
| `pop()` | O(log n) |
| `peek()` | O(1) |
| `is_empty()` | O(1) |
| `__len__()` | O(1) |
| `to_list()` | O(n) |
| Construction from iterable | O(n) |

## Space Complexity

O(n) where n is the number of elements.

## Use Cases

- **Priority Queues** - Task scheduling, event simulation
- **Heap Sort** - Efficient sorting algorithm
- **Top-K Problems** - Finding k largest/smallest elements
- **Median Finding** - Using two heaps
- **Dijkstra's Algorithm** - Shortest path finding

## Example: Priority Queue

```python
class Task:
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name
    
    def __lt__(self, other):
        return self.priority < other.priority
    
    def __repr__(self):
        return f"Task({self.priority}, {self.name})"

# MinHeap for priority queue (lower number = higher priority)
pq = MinHeap([
    Task(3, "Low priority"),
    Task(1, "High priority"),
    Task(2, "Medium priority")
])

# Process tasks in priority order
while not pq.is_empty():
    task = pq.pop()
    print(f"Processing: {task.name}")
```

## Example: Top-K Elements

```python
def find_top_k_largest(items, k):
    """Find k largest elements using MinHeap."""
    min_heap = MinHeap()
    
    for item in items:
        if len(min_heap) < k:
            min_heap.push(item)
        elif item > min_heap.peek():
            min_heap.pop()
            min_heap.push(item)
    
    # Return in descending order
    result = []
    while not min_heap.is_empty():
        result.append(min_heap.pop())
    return result[::-1]

top_3 = find_top_k_largest([1, 5, 3, 9, 2, 7, 4, 8], 3)
# Returns [9, 8, 7]
```

## Example: Heap Sort

```python
def heap_sort(items):
    """Sort items using heap."""
    heap = MinHeap(items)
    result = []
    
    while not heap.is_empty():
        result.append(heap.pop())
    
    return result

sorted_items = heap_sort([3, 1, 4, 1, 5, 9, 2, 6])
# Returns [1, 1, 2, 3, 4, 5, 6, 9]
```

## Example: Finding Median

```python
class MedianFinder:
    def __init__(self):
        # MaxHeap for lower half (largest at root)
        self.lower = MaxHeap()
        # MinHeap for upper half (smallest at root)
        self.upper = MinHeap()
    
    def add(self, num):
        if self.lower.is_empty() or num <= self.lower.peek():
            self.lower.push(num)
        else:
            self.upper.push(num)
        
        # Balance heaps
        if len(self.lower) > len(self.upper) + 1:
            self.upper.push(self.lower.pop())
        elif len(self.upper) > len(self.lower) + 1:
            self.lower.push(self.upper.pop())
    
    def find_median(self):
        if len(self.lower) == len(self.upper):
            return (self.lower.peek() + self.upper.peek()) / 2
        elif len(self.lower) > len(self.upper):
            return self.lower.peek()
        else:
            return self.upper.peek()
```

## Internal Structure

Heaps are typically implemented using arrays:

- Parent of node at index `i`: `(i - 1) // 2`
- Left child of node at index `i`: `2 * i + 1`
- Right child of node at index `i`: `2 * i + 2`

## Heap Operations

### Heapify Up (Bubble Up)

After inserting, move element up until heap property is satisfied:

```python
def heapify_up(heap, index):
    parent = (index - 1) // 2
    if parent >= 0 and heap[parent] > heap[index]:
        heap[parent], heap[index] = heap[index], heap[parent]
        heapify_up(heap, parent)
```

### Heapify Down (Bubble Down)

After removing root, move element down until heap property is satisfied:

```python
def heapify_down(heap, index):
    left = 2 * index + 1
    right = 2 * index + 2
    smallest = index
    
    if left < len(heap) and heap[left] < heap[smallest]:
        smallest = left
    if right < len(heap) and heap[right] < heap[smallest]:
        smallest = right
    
    if smallest != index:
        heap[index], heap[smallest] = heap[smallest], heap[index]
        heapify_down(heap, smallest)
```
