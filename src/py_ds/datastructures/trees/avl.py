from py_ds.datastructures.trees.base import T, _BinaryNode
from py_ds.datastructures.trees.binary_search_tree import BinarySearchTree


class AVLTree(BinarySearchTree[T]):
    def _balance_factor(self, node: _BinaryNode[T]):
        return self._height(node.left) - self._height(node.right)
