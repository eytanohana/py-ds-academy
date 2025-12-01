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
            self._length += 1


    def prepend(self, value: T) -> None:
        """
        Add a value to the beginning of the list.

        Time complexity: O(1).
        """

    def insert(self, index: int, value: T) -> None:
        """
        Insert a value at a specific index.

        Raises:
            IndexError: if index is out of bounds.
        """

    def remove(self, value: T) -> None:
        """
        Remove the first occurrence of `value` from the list.

        Raises:
            ValueError: if the value is not found.
        """

    def pop(self, index: int = -1) -> T:
        """
        Remove and return the item at the given index.

        Args:
            index: 0-based index, negative indexes supported (Python style).
        Raises:
            IndexError: if the list is empty or index invalid.
        """

    def clear(self) -> None:
        """Remove all elements."""

    # ---------------------------------------------------
    # Access helpers
    # ---------------------------------------------------

    def head(self) -> Optional[T]:
        """Return the first value, or None if list is empty."""

    def tail(self) -> Optional[T]:
        """
        Return the last value, or None if empty.

        Time complexity: O(1) thanks to tail pointer.
        """

    # ---------------------------------------------------
    # Python protocol methods
    # ---------------------------------------------------

    def __iter__(self) -> Iterator[T]:
        """Iterate through values head → tail."""

    def reverse_iter(self) -> Iterator[T]:
        """Iterate through values tail → head (doubly linked list advantage)."""

    def __setitem__(self, index: int, value: T) -> None:
        """
        Set item at index.

        Raises:
            IndexError
        """
