from py_ds.datastructures.trees.base import T, _BinaryNode
from py_ds.datastructures.trees.binary_search_tree import BinarySearchTree


class AVLTree(BinarySearchTree[T]):
    def _height(self, node: _BinaryNode[T] | None) -> int:
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))

    def _balance_factor(self, node: _BinaryNode[T]) -> int:
        return self._height(node.left) - self._height(node.right)

    @staticmethod
    def _rotate_right(node: _BinaryNode[T]) -> _BinaryNode[T]:
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root

    @staticmethod
    def _rotate_left(node: _BinaryNode[T]) -> _BinaryNode[T]:
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root

    def _rotate_left_right(self, node: _BinaryNode[T]) -> None:
        node.left = self._rotate_left(node.left)
        return self._rotate_right(node)

    def _rotate_right_left(self, node: _BinaryNode[T]) -> None:
        node.right = self._rotate_right(node.right)
        return self._rotate_left(node)

    def _rebalance(self, node: _BinaryNode[T]) -> _BinaryNode[T]:
        bf = self._balance_factor(node)
        if bf > 1:
            if self._balance_factor(node.left) > 0:
                return self._rotate_right(node)
            return self._rotate_left_right(node)

        if bf < -1:
            if self._balance_factor(node.right) < 0:
                return self._rotate_left(node)
            return self._rotate_right_left(node)
        return node

    def _insert_recursive(self, node: _BinaryNode[T] | None, value: T) -> _BinaryNode[T]:
        if node is None:
            return _BinaryNode(value=value)
        if value <= node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)
        return self._rebalance(node)

    def _remove_recursive(self, node: _BinaryNode[T] | None, value: T) -> tuple[_BinaryNode[T] | None, bool]:
        if node is None:
            return None, False

        if value < node.value:
            node.left, removed = self._remove_recursive(node.left, value)
        elif value > node.value:
            node.right, removed = self._remove_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right, True
            elif node.right is None:
                return node.left, True

            temp = self._get_min_node(node.right)
            node.value = temp.value
            node.right, _ = self._remove_recursive(node.right, temp.value)
            removed = True

        return self._rebalance(node), removed

    def remove(self, value: T) -> None:
        self._root, removed = self._remove_recursive(self._root, value)
        if removed:
            self.size -= 1

    def insert(self, value: T) -> None:
        self._root = self._insert_recursive(self._root, value)
        self.size += 1
