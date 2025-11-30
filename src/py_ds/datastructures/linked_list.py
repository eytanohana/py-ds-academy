from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Iterable, Iterator, Optional, TypeVar

T = TypeVar("T")


@dataclass
class _Node(Generic[T]):
    """A single node in the linked list."""
    value: T
    next: Optional[_Node[T]] = None


class SinglyLinkedList(Generic[T]):
    """
    A singly linked list supporting typical operations:
    - append / prepend
    - insert at index
    - remove by value
    - iteration
    - length, truthiness
    """

    def __init__(self, items: Iterable[T] | None = None) -> None:
        """
        Initialize the list with optional items.
        Items are appended in order (first item becomes head).
        """
        self._head: Optional[_Node[T]] = None
        self._length: int = 0
        for item in items or []:
            self.append(item)

    # ---------------------------------------------------
    # Core list operations
    # ---------------------------------------------------

    def append(self, value: T) -> None:
        """
        Add a value to the end of the list.

        Time complexity: O(n).
        """
        new_node = _Node(value=value)
        if self._head is None:
            self._head = new_node
        else:
            curr = self._head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self._length += 1

    def prepend(self, value: T) -> None:
        """
        Add a value to the beginning of the list.

        Time complexity: O(1).
        """
        new_node = _Node(value=value)
        if self._head is None:
            self._head = new_node
        else:
            new_node.next = self._head
            self._head = new_node
        self._length += 1

    def insert(self, index: int, value: T) -> None:
        """
        Insert a value at a specific index.

        Raises:
            IndexError: if index is out of bounds.
        """
        if index < 0 or index > self._length:
            raise IndexError('index out of bounds on list')
        if index == 0:
            self.prepend(value)
        elif index == self._length:
            self.append(value)
        else:
            prev, curr, idx = None, self._head, 0
            for _ in range(index):
                prev = curr
                curr = curr.next
            new_node = _Node(value=value)
            new_node.next = curr
            prev.next = new_node
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
        if curr and curr.value == value:
            if prev:
                prev.next = curr.next
            else:
                self._head = self._head.next
            self._length -= 1
        else:
            raise ValueError('value not found')

    def pop(self, index: int = -1) -> T:
        """
        Remove and return the item at the given index.

        Args:
            index: 0-based index, negative indexes supported (Python style).
        Raises:
            IndexError: if the list is empty or index invalid.
        """
        prev, curr = None, self._head
        idx = self._length + index if index < 0 else index
        if idx < 0 or idx >= self._length or self._length == 0:
            raise IndexError('invalid index')
        for i in range(idx):
            prev = curr
            curr = curr.next
        if prev:
            prev.next = curr.next
        else:
            self._head = None
        self._length -= 1
        return curr.value

    def find(self, value: T) -> int:
        """
        Return the index of the first occurrence of `value`.

        Returns:
            index (int)

        Raises:
            ValueError: if value is not found.
        """
        for i, node_value in enumerate(self):
            if value == node_value:
                return i
        raise ValueError('value not found')

    def clear(self) -> None:
        """Remove all elements."""
        self._head = None
        self._length = 0

    # ---------------------------------------------------
    # Access helpers
    # ---------------------------------------------------

    def head(self) -> Optional[T]:
        """Return the first value, or None if list is empty."""
        return self._head.value if self._head else None

    def tail(self) -> Optional[T]:
        """Return the last value, or None if empty."""
        if not self._head:
            return None
        curr = self._head
        while curr and curr.next:
            curr = curr.next
        return curr.value

    def to_list(self) -> list[T]:
        """Return Python list of all values in order."""
        return list(self)

    # ---------------------------------------------------
    # Python protocol methods
    # ---------------------------------------------------

    def __len__(self) -> int:
        """Return number of elements."""
        return self._length

    def __bool__(self) -> bool:
        """Truthiness: empty list is False; otherwise True."""
        return self._length > 0

    def __iter__(self) -> Iterator[T]:
        """Iterate through values head → tail."""
        curr = self._head
        while curr:
            yield curr.value
            curr = curr.next

    def __getitem__(self, index: int) -> T:
        """
        Indexing support.

        Raises:
            IndexError
        """
        if index < 0 or index >= len(self):
            raise IndexError('bad index')
        for i, value in enumerate(self):
            if i == index:
                return value

    def __setitem__(self, index: int, value: T) -> None:
        """
        Set item at index.

        Raises:
            IndexError
        """
        if index < 0 or index >= self._length:
            raise IndexError('bad index')
        idx, curr = 0, self._head
        while idx < index:
            curr = curr.next
        curr.value = value

    def __repr__(self) -> str:
        """
        Representation:

            SinglyLinkedList([1, 2, 3])
        """
        return f"SinglyLinkedList({self.to_list()})"
