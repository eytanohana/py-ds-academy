from collections.abc import Iterable, Iterator

from py_ds.datastructures.linked_lists.base import LinkedListBase, T, _Node


class SinglyLinkedList(LinkedListBase[T]):
    """
    A singly linked list supporting typical operations:
    - append / prepend
    - insert at index
    - remove by value
    - iteration
    - length, truthiness
    """

    def __init__(self, items: Iterable[T] | None = None) -> None:
        """
        Initialize the list with optional items.
        Items are appended in order (first item becomes head).
        """
        self._head: _Node[T] | None = None
        super().__init__(items)

    # ---------------------------------------------------
    # Core list operations
    # ---------------------------------------------------

    def append(self, value: T) -> None:
        """
        Add a value to the end of the list.

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
        """
        Add a value to the beginning of the list.

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
        """
        Insert a value at a specific index.

        Raises:
            IndexError: if index is out of bounds.
        """
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
        """
        Remove the first occurrence of `value` from the list.

        Raises:
            ValueError: if the value is not found.
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
        """
        Remove and return the item at the given index.

        Args:
            index: 0-based index, negative indexes supported (Python style).
        Raises:
            IndexError: if the list is empty or index invalid.
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
        """Remove all elements."""
        self._head = None
        self._length = 0

    # ---------------------------------------------------
    # Access helpers
    # ---------------------------------------------------

    def head(self) -> T | None:
        """Return the first value, or None if list is empty."""
        return self._head.value if self._head else None

    def tail(self) -> T | None:
        """Return the last value, or None if empty."""
        if not self._head:
            return None
        curr = self._head
        while curr and curr.next:
            curr = curr.next
        return curr.value

    # ---------------------------------------------------
    # Python protocol methods
    # ---------------------------------------------------

    def __iter__(self) -> Iterator[T]:
        """Iterate through values head → tail."""
        curr = self._head
        while curr:
            yield curr.value
            curr = curr.next

    def __setitem__(self, index: int, value: T) -> None:
        """
        Set item at index.

        Raises:
            IndexError
        """
        if index < 0 or index >= self._length:
            raise IndexError('bad index')
        idx, curr = 0, self._head
        while idx < index:
            curr = curr.next
        curr.value = value
