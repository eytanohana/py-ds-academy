from __future__ import annotations

from collections.abc import Iterable, Iterator
from dataclasses import dataclass

from py_ds.datastructures.linked_lists.singly_linked import LinkedList, T, _Node


@dataclass
class _DoublyNode(_Node[T]):
    """A node in the doubly linked list."""

    prev: _DoublyNode[T] | None = None


class DoublyLinkedList(LinkedList[T]):
    """A doubly linked list with forward and backward links.

    Advantages over singly linked list include O(1) append (with tail pointer),
    O(1) tail access, bidirectional traversal, and more efficient deletion
    when node reference is known.
    """

    def __init__(self, items: Iterable[T] | None = None) -> None:
        """Initialize the doubly linked list with optional items.

        Args:
            items: Optional iterable of items to initialize the list with.
        """
        self._head: _DoublyNode[T] | None = None
        self._tail: _DoublyNode[T] | None = None
        super().__init__(items)

    def append(self, value: T) -> None:
        """Add a value to the end of the list.

        Args:
            value: The value to append to the list.

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
        """Add a value to the beginning of the list.

        Args:
            value: The value to prepend to the list.

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
        """Get the node at the specified index.

        Uses bidirectional traversal for efficiency when accessing nodes near
        the tail.

        Args:
            index: The position of the node to retrieve. Supports negative indexing.

        Returns:
            The node at the specified index.

        Raises:
            IndexError: If the list is empty or index is out of bounds.

        Time complexity: O(n).
        """
        self._validate_index(index)
        if index < 0:
            index = self._length + index

        if index <= self._length // 2:
            return super()._get_node_at(index)

        curr = self._tail
        for _ in range(self._length - index - 1):
            curr = curr.prev
        return curr

    def insert(self, index: int, value: T) -> None:
        """Insert a value at a specific index.

        Args:
            index: The position at which to insert the value.
            value: The value to insert.

        Raises:
            IndexError: If index is out of bounds.

        Time complexity: O(n).
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
        """Remove the first occurrence of `value` from the list.

        Args:
            value: The value to remove from the list.

        Raises:
            ValueError: If the value is not found.

        Time complexity: O(n).
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
        """Remove and return the item at the given index.

        Args:
            index: 0-based index, negative indexes supported (Python style).
                Defaults to -1 (last element).

        Returns:
            The value at the specified index.

        Raises:
            IndexError: If the list is empty or index is invalid.

        Time complexity: O(n).
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
        """Remove all elements from the list.

        Time complexity: O(n).
        """
        self._head = self._tail = None
        self._length = 0

    def head(self) -> T | None:
        """Return the first value in the list.

        Returns:
            The first value in the list, or None if the list is empty.

        Time complexity: O(1).
        """
        return self._head.value if self._head else None

    def tail(self) -> T | None:
        """Return the last value in the list.

        Returns:
            The last value in the list, or None if the list is empty.

        Time complexity: O(1).
        """
        return self._tail.value if self._tail else None

    def reverse_iter(self) -> Iterator[T]:
        """Iterate through values from tail to head.

        This is a doubly linked list advantage, allowing efficient reverse
        traversal.

        Yields:
            The values in the list from tail to head.

        Time complexity: O(n).
        """
        curr = self._tail
        while curr:
            yield curr.value
            curr = curr.prev

    def __str__(self) -> str:
        """Return a string representation of the linked list.

        Returns:
            A visual representation of the linked list.

        Time complexity: O(n).
        """
        if not self:
            return 'HEAD ⇆ TAIL'
        return 'HEAD ⇆ ' + ' ⇆ '.join(str(item) for item in self) + ' ⇆ TAIL'
