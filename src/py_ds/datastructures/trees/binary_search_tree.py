from collections.abc import Iterator

from py_ds.datastructures.trees.base import BinaryTree, T, _BinaryNode


class BinarySearchTree(BinaryTree[T]):
    def insert(self, value: T) -> None:
        insert_node = _BinaryNode(value=value)
        if self._root is None:
            self._root = insert_node
            return
        curr = self._root
        while True:
            if value <= curr.value:
                if curr.left is None:
                    curr.left = insert_node
                    break
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = insert_node
                    break
                curr = curr.right
        self.size += 1

    def remove(self, value: T) -> None:
        pass

    def clear(self) -> None:
        pass

    def __iter__(self) -> Iterator[T]:
        pass
