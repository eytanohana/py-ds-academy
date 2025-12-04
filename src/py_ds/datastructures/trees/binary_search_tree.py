from collections.abc import Iterator

from py_ds.datastructures.trees.base import BinaryTree, T, _BinaryNode


class BinarySearchTree(BinaryTree[T]):
    def insert(self, value: T) -> None:
        insert_node = _BinaryNode(value=value)
        self.size += 1
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

    def remove(self, value: T) -> None:
        pass

    def clear(self) -> None:
        pass

    def __iter__(self) -> Iterator[T]:
        pass

    def min(self) -> T:
        if self.is_empty:
            raise ValueError("Empty tree")
        curr = self._root
        while curr.left:
            curr = curr.left
        return curr.value

    def max(self) -> T:
        if self.is_empty:
            raise ValueError("Empty tree")
        curr = self._root
        while curr.right:
            curr = curr.right
        return curr.value
