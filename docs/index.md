# py-ds-academy

<div align="center" markdown>

![PyPI - Version](https://img.shields.io/pypi/v/py-ds-academy)
![PyPI - License](https://img.shields.io/pypi/l/py-ds-academy)
[![CI status](https://github.com/eytanohana/py-ds-academy/actions/workflows/ci.yml/badge.svg)](https://github.com/eytanohana/py-ds-academy/actions/workflows/ci.yml)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/py-ds-academy)

**Data structures implemented from scratch for learning and experimentation**

</div>

---

## 🎯 About

**py-ds-academy** is a comprehensive collection of classic data structures implemented from scratch in Python. The goal is **learning + correctness** (with tests), not squeezing out every last micro-optimization.

This project serves as both a learning resource and a reference implementation for common data structures used in computer science and software engineering.

## ✨ Features

- 🧱 **Core Data Structures** - Stacks, queues, linked lists, trees, and heaps
- 📝 **Type Hints** - Full type annotations for better code clarity
- 🧪 **Comprehensive Tests** - TDD-first approach with pytest
- 📚 **Well Documented** - Clear APIs with complexity notes
- 🎓 **Educational** - Perfect for learning data structures

## 🚀 Quick Start

```bash
# Install dependencies
uv sync

# Run tests
uv run pytest

# Try it out
uv run python
```

```python
>>> from py_ds import Stack, Queue, MinHeap, BinarySearchTree

>>> # Stack example
>>> s = Stack([1, 2, 3])
>>> s.pop()
3

>>> # Queue example
>>> q = Queue([1, 2, 3])
>>> q.dequeue()
1

>>> # Heap example
>>> h = MinHeap([3, 1, 4, 1, 5])
>>> h.pop()
1
```

## 📦 Implemented Data Structures

### Linear Structures

- ✅ **Stack** - LIFO stack with list backing
- ✅ **Queue** - FIFO queue with list backing
- ✅ **LinkedList** - Single-direction linked list
- ✅ **DoublyLinkedList** - Double-direction linked list

### Trees

- ✅ **BinaryTree** - Generic binary tree with multiple traversal methods
- ✅ **BinarySearchTree** - Binary search tree with insert, remove, search
- ✅ **AVLTree** - Self-balancing AVL tree

### Heaps

- ✅ **MinHeap** - Minimum binary heap
- ✅ **MaxHeap** - Maximum binary heap

## 🎓 Learning Resources

This project is designed to help you:

- Understand how data structures work under the hood
- Learn time and space complexity analysis
- Practice clean code and type hints
- See real-world implementations with tests

## 📚 Documentation

Explore the documentation to learn more:

- **[Getting Started](getting-started/installation.md)** - Installation and setup
- **[Data Structures](structures/index.md)** - Overview of all implemented structures
- **[API Reference](reference/index.md)** - Complete API documentation

## 🤝 Contributing

Contributions are welcome! See the [Contributing Guide](contributing.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/eytanohana/py-ds-academy/blob/main/LICENSE) file for details.

---

<div align="center" markdown>

Made with ❤️ by [Eytan Ohana](https://github.com/eytanohana)

</div>
