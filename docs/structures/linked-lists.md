# Linked Lists

**Linked Lists** are dynamic data structures that store elements in nodes connected by pointers. Unlike arrays, linked lists don't require contiguous memory allocation.

## Overview

py-ds-academy provides two implementations:

- **SinglyLinkedList** - Each node points only to the next node
- **DoublyLinkedList** - Each node points to both next and previous nodes

## Singly Linked List

A linear data structure where each node contains data and a reference to the next node.

### Operations

```python
from py_ds import SinglyLinkedList

# Create a linked list
sll = SinglyLinkedList([1, 2, 3])

# Append at the end
sll.append(4)  # O(n) - must traverse to end

# Prepend at the beginning
sll.prepend(0)  # O(1)

# Insert at index
sll.insert(2, 99)  # O(n)

# Remove by value
sll.remove(2)  # O(n)

# Pop from end
item = sll.pop()  # O(n)

# Find an element
node = sll.find(3)  # O(n)

# Access by index
value = sll[0]  # O(n)
sll[0] = 10  # O(n)

# Get head and tail
head = sll.head()
tail = sll.tail()

# Clear all nodes
sll.clear()
```

### Time Complexity

| Operation | Time Complexity |
|-----------|----------------|
| `append(item)` | O(n) |
| `prepend(item)` | O(1) |
| `insert(index, item)` | O(n) |
| `remove(item)` | O(n) |
| `pop()` | O(n) |
| `find(item)` | O(n) |
| `__getitem__(index)` | O(n) |
| `__setitem__(index, item)` | O(n) |
| `head()` | O(1) |
| `tail()` | O(n) |

## Doubly Linked List

A linked list where each node contains references to both next and previous nodes, enabling efficient bidirectional traversal.

### Operations

```python
from py_ds import DoublyLinkedList

# Create a doubly linked list
dll = DoublyLinkedList([1, 2, 3])

# Append at the end (O(1) with tail pointer!)
dll.append(4)  # O(1)

# Prepend at the beginning
dll.prepend(0)  # O(1)

# Insert at index
dll.insert(2, 99)  # O(n) - optimized with bidirectional search

# Remove by value
dll.remove(2)  # O(n)

# Pop from end
item = dll.pop()  # O(1)

# Find an element
node = dll.find(3)  # O(n)

# Access by index (optimized)
value = dll[0]  # O(n) - but uses bidirectional search
dll[0] = 10  # O(n)

# Forward iteration
for item in dll:
    print(item)

# Reverse iteration
for item in dll.reverse_iter():
    print(item)

# Get head and tail
head = dll.head()
tail = dll.tail()  # O(1)
```

### Time Complexity

| Operation | Time Complexity |
|-----------|----------------|
| `append(item)` | O(1) ⚡ |
| `prepend(item)` | O(1) |
| `insert(index, item)` | O(n) |
| `remove(item)` | O(n) |
| `pop()` | O(1) ⚡ |
| `find(item)` | O(n) |
| `__getitem__(index)` | O(n) |
| `__setitem__(index, item)` | O(n) |
| `head()` | O(1) |
| `tail()` | O(1) ⚡ |
| `reverse_iter()` | O(n) |

⚡ = Advantage over singly linked list

## Space Complexity

O(n) where n is the number of elements. DoublyLinkedList uses slightly more memory due to the extra pointer per node.

## Use Cases

- **Dynamic Memory Allocation** - When size is unknown at compile time
- **Implementing Other Structures** - Stacks, queues, deques
- **Insertion/Deletion Heavy** - When frequent insertions/deletions are needed
- **Undo/Redo** - DoublyLinkedList enables efficient backward traversal
- **Browser History** - Forward/backward navigation

## Example: Implementing a Stack with Linked List

```python
class LinkedListStack:
    def __init__(self):
        self._list = SinglyLinkedList()
    
    def push(self, item):
        self._list.prepend(item)
    
    def pop(self):
        if self._list.head() is None:
            raise IndexError("Stack is empty")
        return self._list.pop(0)
    
    def peek(self):
        head = self._list.head()
        if head is None:
            raise IndexError("Stack is empty")
        return head.value
```

## Example: Browser History

```python
class BrowserHistory:
    def __init__(self):
        self.history = DoublyLinkedList()
        self.current = None
    
    def visit(self, url):
        if self.current:
            # Remove all forward history
            while self.history.tail() != self.current:
                self.history.pop()
        self.history.append(url)
        self.current = self.history.tail()
    
    def back(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            return self.current.value
        return None
    
    def forward(self):
        if self.current and self.current.next:
            self.current = self.current.next
            return self.current.value
        return None
```

## When to Use Which?

**Use SinglyLinkedList when:**
- You only need forward traversal
- Memory is a concern
- You're implementing a simple stack or queue

**Use DoublyLinkedList when:**
- You need efficient append operations
- You need bidirectional traversal
- You're implementing undo/redo functionality
- You need efficient tail access
