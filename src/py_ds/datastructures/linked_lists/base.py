from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar('T')


@dataclass
class _Node(Generic[T]):
    """A node in the singly linked list.

    Attributes:
        value: The data stored in the node.
        next: Reference to the next node in the list, or None if this is the last node.
    """

    value: T
    next: _Node[T] | None = None


class LinkedListBase(ABC, Generic[T]):
    """Abstract base class for linked list implementations.

    Defines the common interface and shares implementations where possible.
    This class provides a foundation for both singly and doubly linked list
    implementations.
    """

    def __init__(self, items: Iterable[T] | None = None) -> None:
        """Initialize the list with optional items.

        Args:
            items: Optional iterable of items to initialize the list with.
                If None, creates an empty list.
        """
        self._head: _Node[T] | None = None
        self._length: int = 0
        for item in items or []:
            self.append(item)

    @abstractmethod
    def append(self, value: T) -> None:
        """Add a value to the end of the list.

        Args:
            value: The value to append to the list.
        """

    @abstractmethod
    def prepend(self, value: T) -> None:
        """Add a value to the beginning of the list.

        Args:
            value: The value to prepend to the list.
        """

    @abstractmethod
    def insert(self, index: int, value: T) -> None:
        """Insert a value at a specific index.

        Args:
            index: The index at which to insert the value.
            value: The value to insert.

        Raises:
            IndexError: If the index is out of range.
        """

    @abstractmethod
    def remove(self, value: T) -> None:
        """Remove the first occurrence of a value.

        Args:
            value: The value to remove from the list.

        Raises:
            ValueError: If the value is not found in the list.
        """

    @abstractmethod
    def pop(self, index: int = -1) -> T:
        """Remove and return the item at the given index.

        Args:
            index: The index of the item to remove. Defaults to -1 (last item).

        Returns:
            The value that was removed from the list.

        Raises:
            IndexError: If the index is out of range.
        """

    @abstractmethod
    def clear(self) -> None:
        """Remove all elements from the list."""

    @abstractmethod
    def head(self) -> T | None:
        """Return the first value in the list.

        Returns:
            The first value in the list, or None if the list is empty.
        """

    @abstractmethod
    def tail(self) -> T | None:
        """Return the last value in the list.

        Returns:
            The last value in the list, or None if the list is empty.
        """

    def __iter__(self) -> Iterator[T]:
        """Iterate through values in the list.

        Yields:
            The values in the list from head to tail.
        """
        curr = self._head
        while curr:
            yield curr.value
            curr = curr.next

    # ---------------------------------------------------
    # Concrete methods (shared implementations)
    # ---------------------------------------------------

    def find(self, value: T) -> int:
        """Return the index of the first occurrence of a value.

        Args:
            value: The value to search for.

        Returns:
            The index of the first occurrence of the value.

        Raises:
            ValueError: If the value is not found in the list.
        """
        for i, node_value in enumerate(self):
            if value == node_value:
                return i
        raise ValueError('value not found')

    def to_list(self) -> list[T]:
        """Convert the linked list to a Python list.

        Returns:
            A Python list containing all values in the linked list, in order
            from head to tail.
        """
        return list(self)

    def __len__(self) -> int:
        """Return the number of elements in the list.

        Returns:
            The number of elements in the linked list.
        """
        return self._length

    def __bool__(self) -> bool:
        """Return the truthiness of the list.

        Returns:
            False if the list is empty, True otherwise.
        """
        return self._length > 0

    def __getitem__(self, index: int) -> T:
        """Get the value at the given index.

        Args:
            index: 0-based index, negative indexes supported (Python style).

        Returns:
            The value at the specified index.

        Raises:
            IndexError: If the index is out of range.
        """
        return self._get_node_at(index).value

    def __repr__(self) -> str:
        """Return a string representation of the linked list.

        Returns:
            A string representation showing the class name and list contents.
        """
        return f'{self.__class__.__name__}({self.to_list()})'

    def _validate_index(self, index: int) -> None:
        if self._length == 0:
            raise IndexError('empty list')
        if index < -self._length or index >= self._length:
            raise IndexError('invalid index')

    def _get_node_at(self, index: int) -> _Node[T]:
        """Get the node at the specified index.

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

        curr = self._head
        for _ in range(index):
            curr = curr.next
        return curr
