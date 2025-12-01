from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from typing import Optional

from py_ds.datastructures.linked_list.base import _Node, T, LinkedListBase


@dataclass
class _DoublyNode(_Node[T]):
    """
    A node in the doubly linked list.
    """
    prev: Optional[_DoublyNode[T]] = None


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
        self._head: Optional[_DoublyNode[T]] = None
        self._tail: Optional[_DoublyNode[T]] = None
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

    def insert(self, index: int, value: T) -> None:
        """
        Insert a value at a specific index.

        Raises:
            IndexError: if index is out of bounds.
        """
        if index < 0 or index > self._length:
            raise IndexError('index out of bounds')

        node = _DoublyNode(value)
        if index == 0:
            self.prepend(value)
            return
        elif index == self._length:
            self.append(value)
            return

        if index > self._length // 2:
            backwards_index = self._length - index
            curr, next_ = self._tail, None
            for _ in range(backwards_index):
                next_ = curr
                curr = curr.prev
            curr.next = node
            node.prev = curr
            node.next = next_
            next_.prev = node
        else:
            prev, curr = None, self._head
            for _ in range(index):
                prev = curr
                curr = curr.next
            prev.next = node
            node.prev = prev
            node.next = curr
            curr.prev = node
        self._length += 1

    def remove(self, value: T) -> None:
        """
        Remove the first occurrence of `value` from the list.

        Raises:
            ValueError: if the value is not found.
        """
        prev, curr = None, self._head
        while curr and curr.value != value:
            prev = curr
            curr = curr.next
        if curr is None or curr.value != value:
            raise ValueError("value not found")

        if prev is not None:
            prev.next = curr.next
            if curr.next:
                curr.next.prev = prev
            else:
                self._tail = prev
        else:
            self._head = curr.next
        self._length -= 1

    def pop(self, index: int = -1) -> T:
        """
        Remove and return the item at the given index.

        Args:
            index: 0-based index, negative indexes supported (Python style).
        Raises:
            IndexError: if the list is empty or index invalid.
        """
        if self._length == 0:
            raise IndexError('pop from an empty list')
        if index < -self._length or index >= self._length:
            raise IndexError('invalid index')

        real_index = self._length + index if index < 0 else index
        if real_index > self._length // 2:
            steps = self._length - real_index - 1
            curr = self._tail
            for _ in range(steps):
                curr = curr.prev
        else:
            curr = self._head
            for _ in range(real_index):
                curr = curr.next

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

    def head(self) -> Optional[T]:
        """Return the first value, or None if list is empty."""
        return self._head.value if self._head else None

    def tail(self) -> Optional[T]:
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
        if index < -self._length or index >= self._length:
            raise IndexError('bad index')
        if index >= 0:
            return super().__getitem__(index)
        for i, value in enumerate(self.reverse_iter()):
            if i == -index - 1:
                return value

    def __setitem__(self, index: int, value: T) -> None:
        """
        Set item at index.

        Raises:
            IndexError
        """
        if self._length == 0:
            raise IndexError('cant set item on empty list')
        if index < -self._length or index >= self._length:
            raise IndexError('invalid index')

        real_index = self._length + index if index < 0 else index
        if real_index > self._length // 2:
            steps = self._length - real_index - 1
            curr = self._tail
            for _ in range(steps):
                curr = curr.prev
        else:
            curr = self._head
            for _ in range(index):
                curr = curr.next
        curr.value = value
