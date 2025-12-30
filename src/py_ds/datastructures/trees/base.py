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
        """Check if the node has any children.

        Returns:
            True if the node has at least one child (left or right), False otherwise.
        """
        return self.left is not None or self.right is not None


class BinaryTree(ABC, Generic[T]):
    def __init__(self, items: Iterable[T] | None = None):
        """Initialize a binary tree.

        Args:
            items: Optional iterable of items to insert into the tree. If None,
                an empty tree is created.
        """
        self._root: _BinaryNode[T] | None = None
        self.size: int = 0
        items = items or []
        for item in items:
            self.insert(item)

    @abstractmethod
    def insert(self, value: T) -> None:
        """Add a value to the tree.

        Args:
            value: The value to insert into the tree.
        """

    @abstractmethod
    def remove(self, value: T) -> None:
        """Remove a value from the tree.

        Args:
            value: The value to remove from the tree.
        """

    def clear(self) -> None:
        """Remove all elements from the tree."""
        self._root = None
        self.size = 0

    @property
    def is_empty(self) -> bool:
        """Check if the tree is empty.

        Returns:
            True if the tree contains no elements, False otherwise.
        """
        return self.size == 0

    def __len__(self) -> int:
        """Return the number of elements in the tree.

        Returns:
            The number of elements in the tree.
        """
        return self.size

    @property
    def height(self) -> int:
        """Get the height of the tree.

        Returns:
            The height of the tree. Returns -1 for an empty tree, 0 for a tree
            with only a root node, and increases by 1 for each level below.
        """
        if not self._root:
            return -1

        def _height(node: _BinaryNode[T] | None):
            if node is None or not node.has_children:
                return 0
            return 1 + max(_height(node.left), _height(node.right))

        return _height(self._root)

    def inorder(self) -> Iterator[T]:
        """Traverse the tree in inorder (left, root, right).

        Yields:
            Values from the tree in inorder traversal order.
        """

        def _inorder(node: _BinaryNode[T] | None):
            if node is None:
                return
            yield from _inorder(node.left)
            yield node.value
            yield from _inorder(node.right)

        yield from _inorder(self._root)

    def preorder(self) -> Iterator[T]:
        """Traverse the tree in preorder (root, left, right).

        Yields:
            Values from the tree in preorder traversal order.
        """

        def _preorder(node: _BinaryNode[T] | None):
            if node is None:
                return
            yield node.value
            yield from _preorder(node.left)
            yield from _preorder(node.right)

        yield from _preorder(self._root)

    def postorder(self) -> Iterator[T]:
        """Traverse the tree in postorder (left, right, root).

        Yields:
            Values from the tree in postorder traversal order.
        """

        def _postorder(node: _BinaryNode[T] | None):
            if node is None:
                return
            yield from _postorder(node.left)
            yield from _postorder(node.right)
            yield node.value

        yield from _postorder(self._root)

    def level_order(self) -> Iterator[T]:
        """Traverse the tree in level-order (breadth-first).

        Yields:
            Values from the tree in level-order traversal, from top to bottom
            and left to right at each level.
        """
        visited = [self._root] if self._root else []
        while visited:
            node = visited.pop(0)
            yield node.value
            if node.left:
                visited.append(node.left)
            if node.right:
                visited.append(node.right)

    def __str__(self) -> str:
        """Return a string representation of the tree.

        Returns:
            A visual string representation of the tree structure. Returns 'EMPTY'
            if the tree is empty.
        """
        if self._root is None:
            return 'EMPTY'

        def build_tree_str(node: _BinaryNode[T], prefix: str, is_left: bool) -> str:
            tree = ''

            if node.right:
                tree += build_tree_str(node.right, prefix + ('│   ' if is_left else '    '), False)

            tree += prefix + ('└── ' if is_left else '┌── ') + str(node.value) + '\n'

            if node.left:
                tree += build_tree_str(node.left, prefix + ('    ' if is_left else '│   '), True)
            return tree

        result = ''
        if self._root.right:
            right_result = build_tree_str(self._root.right, '', False)
            result += right_result

        result += f'{self._root.value}\n'

        if self._root.left:
            left_result = build_tree_str(self._root.left, '', True)
            result += left_result

        return result
