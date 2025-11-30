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

    def prepend(self, value: T) -> None:
        """
        Add a value to the beginning of the list.

        Time complexity: O(1).
        """

    def insert(self, index: int, value: T) -> None:
        """
        Insert a value at a specific index.

        Args:
            index: 0-based index. If index >= len(list), behaves like append().

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

    def find(self, value: T) -> int:
        """
        Return the index of the first occurrence of `value`.

        Returns:
            index (int)

        Raises:
            ValueError: if value is not found.
        """

    def clear(self) -> None:
        """Remove all elements."""

    # ---------------------------------------------------
    # Access helpers
    # ---------------------------------------------------

    def head(self) -> Optional[T]:
        """Return the first value, or None if list is empty."""

    def tail(self) -> Optional[T]:
        """Return the last value, or None if empty."""

    def to_list(self) -> list[T]:
        """Return Python list of all values in order."""

    # ---------------------------------------------------
    # Python protocol methods
    # ---------------------------------------------------

    def __len__(self) -> int:
        """Return number of elements."""

    def __bool__(self) -> bool:
        """Truthiness: empty list is False; otherwise True."""

    def __iter__(self) -> Iterator[T]:
        """Iterate through values head → tail."""

    def __getitem__(self, index: int) -> T:
        """
        Indexing support.

        Raises:
            IndexError
        """

    def __setitem__(self, index: int, value: T) -> None:
        """
        Set item at index.

        Raises:
            IndexError
        """

    def __repr__(self) -> str:
        """
        Representation:

            SinglyLinkedList([1, 2, 3])
        """
