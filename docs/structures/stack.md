# Stack

A **Stack** is a Last-In-First-Out (LIFO) data structure where elements are added and removed from the same end (the "top").

## Overview

The Stack implementation in py-ds-academy is backed by a Python list, providing O(1) push and pop operations.

## Operations

### Creating a Stack

```python
from py_ds import Stack

# Create an empty stack
stack = Stack()

# Create a stack from an iterable
stack = Stack([1, 2, 3])
```

### Adding Elements

```python
# Push an item onto the stack
stack.push(4)  # O(1)
```

### Removing Elements

```python
# Pop and return the top item
item = stack.pop()  # O(1), raises IndexError if empty
```

### Accessing Elements

```python
# Peek at the top without removing
top = stack.peek()  # O(1), raises IndexError if empty
```

### Utility Methods

```python
# Check if stack is empty
is_empty = stack.is_empty()  # O(1)

# Get the number of elements
length = len(stack)  # O(1)

# Clear all elements
stack.clear()  # O(1)

# Convert to list in order of stack popping
items = list(stack)  # O(n)

# Extend with multiple items
stack.extend([5, 6, 7])  # O(k) where k is number of items
```

### Iteration

```python
# Iterate over stack (from top to bottom)
for item in stack:
    print(item)

# Convert to list
items = list(stack)
```

## Time Complexity

| Operation       | Time Complexity |
|-----------------|-----------------|
| `push(item)`    | O(1)            |
| `pop()`         | O(1)            |
| `peek()`        | O(1)            |
| `is_empty()`    | O(1)            |
| `__len__()`     | O(1)            |
| `clear()`       | O(1)            |
| `extend(items)` | O(k)            |
| `__iter__()`    | O(n)            |
| `__list__()`    | O(n)            |

## Space Complexity

O(n) where n is the number of elements stored.

## Use Cases

- **Expression Evaluation** - Postfix/infix expression parsing
- **Undo/Redo** - Maintaining history in applications
- **Backtracking** - Depth-first search algorithms
- **Function Call Stack** - Managing function calls and local variables
- **Syntax Parsing** - Matching parentheses, brackets, etc.

## Example: Balanced Parentheses

```python
def is_balanced(expression: str) -> bool:
    stack = Stack()
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in expression:
        if char in pairs:
            stack.push(char)
        elif char in pairs.values():
            if stack.is_empty():
                return False
            if pairs[stack.pop()] != char:
                return False
    
    return stack.is_empty()

print(is_balanced("((()))"))  # True
print(is_balanced("((())"))   # False
```

## Example: Postfix Evaluation

```python
def evaluate_postfix(expression: str) -> int:
    stack = Stack()
    
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
    
    return stack.pop()

result = evaluate_postfix("3 4 + 2 *")  # (3+4)*2 = 14
```
