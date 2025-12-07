from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar('T')


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
        self.size = 0
        items = items or []
        for item in items:
            self.insert(item)

    @abstractmethod
    def insert(self, value: T) -> None:
        """Add a value to the end of the tree."""

    @abstractmethod
    def remove(self, value: T) -> None:
        """Remove the first occurrence of a value."""

    def clear(self) -> None:
        self._root = None
        self.size = 0

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
            yield from _inorder(node.left)
            yield node.value
            yield from _inorder(node.right)

        yield from _inorder(self._root)

    def preorder(self) -> Iterator[T]:
        def _preorder(node: _BinaryNode[T] | None):
            if node is None:
                return
            yield node.value
            yield from _preorder(node.left)
            yield from _preorder(node.right)

        yield from _preorder(self._root)

    def postorder(self) -> Iterator[T]:
        def _postorder(node: _BinaryNode[T] | None):
            if node is None:
                return
            yield from _postorder(node.left)
            yield from _postorder(node.right)
            yield node.value

        yield from _postorder(self._root)

    def level_order(self) -> Iterator[T]:
        visited = [self._root] if self._root else []
        while visited:
            node = visited.pop(0)
            yield node.value
            if node.left:
                visited.append(node.left)
            if node.right:
                visited.append(node.right)
