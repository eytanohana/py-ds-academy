from py_ds.datastructures.trees.base import BinaryTree, T, _BinaryNode


class BinarySearchTree(BinaryTree[T]):
    def insert(self, value: T) -> None:
        """Insert a value into the binary search tree.

        The value is inserted according to the binary search tree property:
        values less than or equal to a node go to the left, values greater
        than a node go to the right.

        Args:
            value: The value to insert into the tree.
        """
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
        """Replace a child node with a new node.

        Args:
            parent_node: The parent node containing the child to replace. If None,
                the old_child is assumed to be the root.
            old_child: The child node to be replaced.
            new_child: The new node to replace the old_child with. Can be None
                to remove the child.
        """
        if not parent_node:
            self._root = new_child
        elif parent_node.left is old_child:
            parent_node.left = new_child
        else:
            parent_node.right = new_child

    def remove(self, value: T) -> None:
        """Remove a value from the binary search tree.

        If the value is not found, the tree remains unchanged.

        Args:
            value: The value to remove from the tree.
        """
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
        self._replace_child(succ_parent, succ, succ.right)

    @staticmethod
    def _get_min_node(node: _BinaryNode[T]) -> _BinaryNode[T]:
        """Get the node with the minimum value in a subtree.

        Args:
            node: The root node of the subtree to search.

        Returns:
            The node containing the minimum value in the subtree.
        """
        while node.left is not None:
            node = node.left
        return node

    @staticmethod
    def _get_max_node(node: _BinaryNode[T]) -> _BinaryNode[T]:
        """Get the node with the maximum value in a subtree.

        Args:
            node: The root node of the subtree to search.

        Returns:
            The node containing the maximum value in the subtree.
        """
        while node.right is not None:
            node = node.right
        return node

    def min(self) -> T:
        """Get the minimum value in the tree.

        Returns:
            The minimum value in the tree.

        Raises:
            ValueError: If the tree is empty.
        """
        if self.is_empty:
            raise ValueError('Empty tree')
        return self._get_min_node(self._root).value

    def max(self) -> T:
        """Get the maximum value in the tree.

        Returns:
            The maximum value in the tree.

        Raises:
            ValueError: If the tree is empty.
        """
        if self.is_empty:
            raise ValueError('Empty tree')
        return self._get_max_node(self._root).value

    def __contains__(self, item: T) -> bool:
        """Check if a value is in the tree.

        Args:
            item: The value to search for.

        Returns:
            True if the value is found in the tree, False otherwise.
        """
        if self.is_empty:
            return False
        curr = self._root
        while curr is not None:
            if item == curr.value:
                return True
            curr = curr.left if item < curr.value else curr.right
        return False
