from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class _BinaryNode(Generic[T]):
    """A node with references to its left and right child nodes."""

    value: T
    left: _BinaryNode[T] | None = None
    right: _BinaryNode[T] | None = None

    @property
    def has_children(self) -> bool:
        return self.left is not None or self.right is not None


class BinaryTree(ABC, Generic[T]):
    def __init__(self, items: Iterable[T] | None = None):
        self._root: _BinaryNode[T] = None
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

    def __len__(self):
        return self.size

    @property
    def height(self) -> int:
        if not self._root:
            return -1

        def _height(node: _BinaryNode[T] | None):
            if node is None or not node.has_children:
                return 0
            return 1 + max(_height(node.left), _height(node.right))

        return _height(self._root)

    def inorder(self) -> Iterator[T]:
        def _inorder(node: _BinaryNode[T] | None):
            if node is None:
                return
            _inorder(node.left)
            yield node.value
            _inorder(node.right)

        yield from _inorder(self._root)

    def preorder(self) -> Iterator[T]:
        pass

    def postorder(self) -> Iterator[T]:
        pass

    def level_order(self) -> Iterator[T]:
        pass
