from py_ds.datastructures.trees.base import T, _BinaryNode
from py_ds.datastructures.trees.binary_search_tree import BinarySearchTree


class AVLTree(BinarySearchTree[T]):
    def _balance_factor(self, node: _BinaryNode[T]) -> int:
        return self._height(node.left) - self._height(node.right)

    def _rebalance(self, node: _BinaryNode[T]) -> None: ...

    def _insert_recursive(self, node: _BinaryNode[T] | None, value: T) -> _BinaryNode[T]:
        if node is None:
            return _BinaryNode(value=value)
        if value <= node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)
        self._rebalance(node)

    def insert(self, value: T) -> None:
        self._root = self._insert_recursive(self._root, value)
        self.size += 1
