from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class _Node(Generic[T]):
    """A node with references to its left and right child nodes."""

    value: T
    left: _Node[T] | None = None
    right: _Node[T] | None = None


class BinaryTree(ABC, Generic[T]):
    def __init__(self, items: Iterable[T] | None = None):
        self._root: _Node[T] = None
        items = items or []
        for item in items:
            self.insert(item)
        self.size = len(items)

    @abstractmethod
    def insert(self, value: T) -> None:
        """Add a value to the end of the tree."""

    @abstractmethod
    def remove(self, value: T) -> None:
        """Remove the first occurrence of a value."""

    @abstractmethod
    def clear(self) -> None:
        """Remove all elements."""

    @abstractmethod
    def __iter__(self) -> Iterator[T]:
        """Iterate through values."""

    @property
    def is_empty(self) -> bool:
        return self.size == 0
