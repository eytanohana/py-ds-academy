from __future__ import annotations

from collections.abc import Iterable, Iterator
from dataclasses import dataclass

from py_ds.datastructures.linked_lists.base import LinkedListBase, T, _Node


@dataclass
class _DoublyNode(_Node[T]):
    """
    A node in the doubly linked list.
    """

    prev: _DoublyNode[T] | None = None


class DoublyLinkedList(LinkedListBase[T]):
    """
    A doubly linked list with forward and backward links.

    Advantages over singly linked list:
    - O(1) append (with tail pointer)
    - O(1) tail access
    - Bidirectional traversal
    - More efficient deletion when node reference is known
    """

    def __init__(self, items: Iterable[T] | None = None) -> None:
        """Initialize the doubly linked list with optional items."""
        self._head: _DoublyNode[T] | None = None
        self._tail: _DoublyNode[T] | None = None
        super().__init__(items)

    # ---------------------------------------------------
    # Core list operations
    # ---------------------------------------------------

    def append(self, value: T) -> None:
        """
        Add a value to the end of the list.

        Time complexity: O(1).
        """
        node = _DoublyNode(value)
        if self._head is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            node.prev = self._tail
            self._tail = node
        self._length += 1

    def prepend(self, value: T) -> None:
        """
        Add a value to the beginning of the list.

        Time complexity: O(1).
        """
        node = _DoublyNode(value)
        if self._head is None:
            self._head = self._tail = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node
        self._length += 1

    def _get_node_at(self, index: int) -> _DoublyNode[T]:
        if self._length == 0:
            raise IndexError('pop from an empty list')
        if index < -self._length or index >= self._length:
            raise IndexError('invalid index')

        if index < 0:
            index = self._length + index

        if index > self._length // 2:
            steps = self._length - index - 1
            curr = self._tail
            for _ in range(steps):
                curr = curr.prev
        else:
            curr = self._head
            for _ in range(index):
                curr = curr.next
        return curr

    def insert(self, index: int, value: T) -> None:
        """
        Insert a value at a specific index.

        Raises:
            IndexError: if index is out of bounds.
        """
        if index == self._length:
            self.append(value)
            return

        new_node = _DoublyNode(value)
        index_node = self._get_node_at(index)
        prev = index_node.prev

        new_node.next = index_node
        index_node.prev = new_node

        if prev:
            prev.next = new_node
            new_node.prev = prev
        else:
            self._head = new_node
        self._length += 1

    def remove(self, value: T) -> None:
        """
        Remove the first occurrence of `value` from the list.

        Raises:
            ValueError: if the value is not found.
        """
        curr = self._head
        while curr and curr.value != value:
            curr = curr.next
        if curr is None or curr.value != value:
            raise ValueError('value not found')

        prev = curr.prev
        next_ = curr.next

        if prev:
            prev.next = next_
        else:
            self._head = next_
            if self._head:
                self._head.prev = None

        if next_:
            next_.prev = prev
        else:
            self._tail = prev
            if self._tail:
                self._tail.next = None
        self._length -= 1

    def pop(self, index: int = -1) -> T:
        """
        Remove and return the item at the given index.

        Args:
            index: 0-based index, negative indexes supported (Python style).
        Raises:
            IndexError: if the list is empty or index invalid.
        """
        curr = self._get_node_at(index)
        value = curr.value
        prev, next_ = curr.prev, curr.next

        if prev:
            prev.next = next_
        else:
            self._head = next_

        if next_:
            next_.prev = prev
        else:
            self._tail = prev
        self._length -= 1
        return value

    def clear(self) -> None:
        """Remove all elements."""
        self._head = self._tail = None
        self._length = 0

    # ---------------------------------------------------
    # Access helpers
    # ---------------------------------------------------

    def head(self) -> T | None:
        """Return the first value, or None if list is empty."""
        return self._head.value if self._head else None

    def tail(self) -> T | None:
        """
        Return the last value, or None if empty.

        Time complexity: O(1) thanks to tail pointer.
        """
        return self._tail.value if self._tail else None

    # ---------------------------------------------------
    # Python protocol methods
    # ---------------------------------------------------

    def __iter__(self) -> Iterator[T]:
        """Iterate through values head → tail."""
        curr = self._head
        while curr:
            yield curr.value
            curr = curr.next

    def reverse_iter(self) -> Iterator[T]:
        """Iterate through values tail → head (doubly linked list advantage)."""
        curr = self._tail
        while curr:
            yield curr.value
            curr = curr.prev

    def __getitem__(self, index: int) -> T:
        """
        Indexing support.

        Raises:
            IndexError
        """
        return self._get_node_at(index).value

    def __setitem__(self, index: int, value: T) -> None:
        """
        Set item at index.

        Raises:
            IndexError
        """
        node = self._get_node_at(index)
        node.value = value
