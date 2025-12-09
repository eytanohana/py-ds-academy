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

    def _replace_child(
        self, parent_node: _BinaryNode[T] | None, old_child: _BinaryNode[T], new_child: _BinaryNode[T] | None
    ) -> None:
        if not parent_node:
            self._root = new_child
        elif parent_node.left is old_child:
            parent_node.left = new_child
        else:
            parent_node.right = new_child

    def remove(self, value: T) -> None:
        if self.is_empty:
            return
        current = self._root
        parent: _BinaryNode[T] = None
        while current and current.value != value:
            parent, current = current, (current.left if value <= current.value else current.right)

        if current is None:
            return

        self.size -= 1

        if current.left is None or current.right is None:
            child = current.left if current.left is not None else current.right
            self._replace_child(parent, current, child)
            return

        succ_parent, succ = current, current.right
        while succ.left is not None:
            succ_parent, succ = succ, succ.left

        current.value = succ.value
        if succ_parent.left is succ:
            succ_parent.left = succ.right
        else:
            succ_parent.right = succ.right

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
