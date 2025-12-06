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
        if self.is_empty:
            return
        curr, parent, left = self._root, None, None
        while curr and curr.value != value:
            parent = curr
            left, curr = (True, curr.left) if value < curr.value else (False, curr.right)
        if not curr:
            return
        self.size -= 1
        if not (curr.left or curr.right):
            if curr == self._root:
                self._root = None
            elif left:
                parent.left = None
            else:
                parent.right = None
            return

        if curr.left and curr.right:
            succ_parent = curr
            succ = curr.right
            while succ.left:
                succ_parent = succ
                succ = succ.left
            curr.value = succ.value
            succ_parent.left = None
            return

        if curr.left:
            if left:
                parent.left = curr.left
            else:
                parent.right = curr.left
        else:
            if left:
                parent.left = curr.right
            else:
                parent.right = curr.right

    def min(self) -> T:
        if self.is_empty:
            raise ValueError('Empty tree')
        curr = self._root
        while curr.left:
            curr = curr.left
        return curr.value

    def max(self) -> T:
        if self.is_empty:
            raise ValueError('Empty tree')
        curr = self._root
        while curr.right:
            curr = curr.right
        return curr.value

    def __contains__(self, item: T) -> bool:
        if self.is_empty:
            return False
        curr = self._root
        while curr is not None:
            if item == curr.value:
                return True
            curr = curr.left if item < curr.value else curr.right
        return False
