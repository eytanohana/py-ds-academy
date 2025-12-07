from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar('T')


@dataclass
class _Node(Generic[T]):
    """A node in the singly linked list."""

    value: T
    next: _Node[T] | None = None


class LinkedListBase(ABC, Generic[T]):
    """
    Abstract base class for linked list implementations.
    Defines the common interface and shares implementations where possible.
    """

    def __init__(self, items: Iterable[T] | None = None) -> None:
        """Initialize the list with optional items."""
        self._length: int = 0
        for item in items or []:
            self.append(item)

    @abstractmethod
    def append(self, value: T) -> None:
        """Add a value to the end of the list."""

    @abstractmethod
    def prepend(self, value: T) -> None:
        """Add a value to the beginning of the list."""

    @abstractmethod
    def insert(self, index: int, value: T) -> None:
        """Insert a value at a specific index."""

    @abstractmethod
    def remove(self, value: T) -> None:
        """Remove the first occurrence of a value."""

    @abstractmethod
    def pop(self, index: int = -1) -> T:
        """Remove and return the item at the given index."""

    @abstractmethod
    def clear(self) -> None:
        """Remove all elements."""

    @abstractmethod
    def head(self) -> T | None:
        """Return the first value, or None if list is empty."""

    @abstractmethod
    def tail(self) -> T | None:
        """Return the last value, or None if empty."""

    @abstractmethod
    def __iter__(self) -> Iterator[T]:
        """Iterate through values."""

    # ---------------------------------------------------
    # Concrete methods (shared implementations)
    # ---------------------------------------------------

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

    def to_list(self) -> list[T]:
        """Return Python list of all values in order."""
        return list(self)

    def __len__(self) -> int:
        """Return number of elements."""
        return self._length

    def __bool__(self) -> bool:
        """Truthiness: empty list is False; otherwise True."""
        return self._length > 0

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

    def __repr__(self) -> str:
        """String representation."""
        class_name = self.__class__.__name__
        return f'{class_name}({self.to_list()})'
