from py_ds.datastructures.trees.base import T, _BinaryNode
from py_ds.datastructures.trees.binary_search_tree import BinarySearchTree


class AVLTree(BinarySearchTree[T]):
    def _height(self, node: _BinaryNode[T] | None) -> int:
        """Calculate the height of a node in the tree.

        Args:
            node: The node to calculate the height for. Can be None.

        Returns:
            The height of the node. Returns -1 for None nodes, 0 for leaf nodes,
            and increases by 1 for each level above.
        """
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))

    def _balance_factor(self, node: _BinaryNode[T]) -> int:
        """Calculate the balance factor of a node.

        The balance factor is the difference between the heights of the left
        and right subtrees. A balanced node has a balance factor between -1 and 1.

        Args:
            node: The node to calculate the balance factor for.

        Returns:
            The balance factor (left subtree height - right subtree height).
            Positive values indicate left-heavy, negative values indicate right-heavy.
        """
        return self._height(node.left) - self._height(node.right)

    @staticmethod
    def _rotate_right(node: _BinaryNode[T]) -> _BinaryNode[T]:
        """Perform a right rotation on a node.

        Args:
            node: The node to rotate around.

        Returns:
            The new root node after rotation.
        """
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root

    @staticmethod
    def _rotate_left(node: _BinaryNode[T]) -> _BinaryNode[T]:
        """Perform a left rotation on a node.

        Args:
            node: The node to rotate around.

        Returns:
            The new root node after rotation.
        """
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root

    def _rotate_left_right(self, node: _BinaryNode[T]) -> None:
        """Perform a left-right (double) rotation on a node.

        This is used when the left child is right-heavy. First performs a left
        rotation on the left child, then a right rotation on the node.

        Args:
            node: The node to rotate around.

        Returns:
            The new root node after the double rotation.
        """
        node.left = self._rotate_left(node.left)
        return self._rotate_right(node)

    def _rotate_right_left(self, node: _BinaryNode[T]) -> None:
        """Perform a right-left (double) rotation on a node.

        This is used when the right child is left-heavy. First performs a right
        rotation on the right child, then a left rotation on the node.

        Args:
            node: The node to rotate around.

        Returns:
            The new root node after the double rotation.
        """
        node.right = self._rotate_right(node.right)
        return self._rotate_left(node)

    def _rebalance(self, node: _BinaryNode[T]) -> _BinaryNode[T]:
        """Rebalance a node if it violates the AVL tree property.

        Performs the necessary rotations to restore balance when the balance
        factor is outside the range [-1, 1].

        Args:
            node: The node to rebalance.

        Returns:
            The root node of the rebalanced subtree.
        """
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
        """Recursively insert a value into the AVL tree.

        Args:
            node: The current node in the recursion. Can be None.
            value: The value to insert.

        Returns:
            The root node of the subtree after insertion and rebalancing.
        """
        if node is None:
            return _BinaryNode(value=value)
        if value <= node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)
        return self._rebalance(node)

    def _remove_recursive(self, node: _BinaryNode[T] | None, value: T) -> tuple[_BinaryNode[T] | None, bool]:
        """Recursively remove a value from the AVL tree.

        Args:
            node: The current node in the recursion. Can be None.
            value: The value to remove.

        Returns:
            A tuple containing:
            - The root node of the subtree after removal and rebalancing (or None)
            - A boolean indicating whether the value was successfully removed
        """
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
        """Remove a value from the AVL tree.

        The tree is automatically rebalanced after removal to maintain the AVL
        property. If the value is not found, the tree remains unchanged.

        Args:
            value: The value to remove from the tree.
        """
        self._root, removed = self._remove_recursive(self._root, value)
        if removed:
            self.size -= 1

    def insert(self, value: T) -> None:
        """Insert a value into the AVL tree.

        The tree is automatically rebalanced after insertion to maintain the AVL
        property, ensuring the tree remains balanced.

        Args:
            value: The value to insert into the tree.
        """
        self._root = self._insert_recursive(self._root, value)
        self.size += 1
