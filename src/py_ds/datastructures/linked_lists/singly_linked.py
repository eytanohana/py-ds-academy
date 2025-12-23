from py_ds.datastructures.linked_lists.base import LinkedListBase, T, _Node


class SinglyLinkedList(LinkedListBase[T]):
    """A singly linked list supporting typical operations.

    Supports append/prepend, insert at index, remove by value, iteration,
    and length/truthiness operations.
    """

    # ---------------------------------------------------
    # Core list operations
    # ---------------------------------------------------

    def append(self, value: T) -> None:
        """Add a value to the end of the list.

        Args:
            value: The value to append to the list.

        Time complexity: O(n).
        """
        new_node = _Node(value=value)
        if self._head is None:
            self._head = new_node
        else:
            curr = self._head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self._length += 1

    def prepend(self, value: T) -> None:
        """Add a value to the beginning of the list.

        Args:
            value: The value to prepend to the list.

        Time complexity: O(1).
        """
        new_node = _Node(value=value)
        if self._head is None:
            self._head = new_node
        else:
            new_node.next = self._head
            self._head = new_node
        self._length += 1

    def insert(self, index: int, value: T) -> None:
        """Insert a value at a specific index.

        Args:
            index: 0-based index, negative indexes supported (Python style).
            value: The value to insert.

        Raises:
            IndexError: If index is out of bounds.

        Time complexity: O(n).
        """
        index = self._length + index if index < 0 else index
        if index < 0 or index > self._length:
            raise IndexError('index out of bounds on list')
        if index == 0:
            self.prepend(value)
        elif index == self._length:
            self.append(value)
        else:
            prev, curr = None, self._head
            for _ in range(index):
                prev = curr
                curr = curr.next
            new_node = _Node(value=value)
            new_node.next = curr
            prev.next = new_node
            self._length += 1

    def remove(self, value: T) -> None:
        """Remove the first occurrence of `value` from the list.

        Args:
            value: The value to remove from the list.

        Raises:
            ValueError: If the value is not found.

        Time complexity: O(n).
        """
        prev, curr = None, self._head
        while curr and curr.value != value:
            prev = curr
            curr = curr.next
        if curr and curr.value == value:
            if prev:
                prev.next = curr.next
            else:
                self._head = self._head.next
            self._length -= 1
        else:
            raise ValueError('value not found')

    def pop(self, index: int = -1) -> T:
        """Remove and return the item at the given index.

        Args:
            index: 0-based index, negative indexes supported (Python style).
                Defaults to -1 (last element).

        Returns:
            The value at the specified index.

        Raises:
            IndexError: If the list is empty or index is invalid.

        Time complexity: O(n).
        """
        prev, curr = None, self._head
        idx = self._length + index if index < 0 else index
        if idx < 0 or idx >= self._length or self._length == 0:
            raise IndexError('invalid index')
        for _ in range(idx):
            prev = curr
            curr = curr.next
        if prev:
            prev.next = curr.next
        else:
            self._head = None
        self._length -= 1
        return curr.value

    def clear(self) -> None:
        """Remove all elements from the list.

        Time complexity: O(1).
        """
        self._head = None
        self._length = 0

    # ---------------------------------------------------
    # Access helpers
    # ---------------------------------------------------

    def head(self) -> T | None:
        """Return the first value in the list.

        Returns:
            The first value in the list, or None if the list is empty.

        Time complexity: O(1).
        """
        return self._head.value if self._head else None

    def tail(self) -> T | None:
        """Return the last value in the list.

        Returns:
            The last value in the list, or None if the list is empty.

        Time complexity: O(n).
        """
        if not self._head:
            return None
        curr = self._head
        while curr and curr.next:
            curr = curr.next
        return curr.value

    # ---------------------------------------------------
    # Python protocol methods
    # ---------------------------------------------------

    def __setitem__(self, index: int, value: T) -> None:
        """Set item at the specified index.

        Args:
            index: The position at which to set the value.
            value: The value to set.

        Raises:
            IndexError: If index is out of bounds.

        Time complexity: O(n).
        """
        if index < 0 or index >= self._length:
            raise IndexError('bad index')
        idx, curr = 0, self._head
        while idx < index:
            curr = curr.next
        curr.value = value

    def __str__(self) -> str:
        """Return a string representation of the linked list.

        Returns:
            A visual representation of the linked list.

        Time complexity: O(n).
        """
        if not self:
            return 'HEAD → NULL'
        return 'HEAD → ' + ' → '.join(str(item) for item in self) + ' → NULL'
