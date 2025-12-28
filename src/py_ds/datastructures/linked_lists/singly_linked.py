from __future__ import annotations

from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar('T')


@dataclass
class _Node(Generic[T]):
    """A node in the singly linked list.

    Attributes:
        value: The data stored in the node.
        next: Reference to the next node in the list, or None if this is the last node.
    """

    value: T
    next: _Node[T] | None = None


class LinkedList(Generic[T]):
    """A singly linked list supporting typical operations.

    Supports append/prepend, insert at index, remove by value, iteration,
    and length/truthiness operations.
    """

    def __init__(self, items: Iterable[T] | None = None) -> None:
        """Initialize the list with optional items.

        Args:
            items: Optional iterable of items to initialize the list with.
                If None, creates an empty list.
        """
        self._head: _Node[T] | None = None
        self._tail: _Node[T] | None = None
        self._length: int = 0
        for item in items or []:
            self.append(item)

    def append(self, value: T) -> None:
        """Add a value to the end of the list.

        Args:
            value: The value to append to the list.

        Time complexity: O(n).
        """
        new_node = _Node(value=value)
        if self._head is None:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._length += 1

    def prepend(self, value: T) -> None:
        """Add a value to the beginning of the list.

        Args:
            value: The value to prepend to the list.

        Time complexity: O(1).
        """
        new_node = _Node(value=value)
        if self._head is None:
            self._head = self._tail = new_node
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
        index = self._get_positive_index(index) + int(index < 0)
        if index < 0 or index > self._length:
            raise IndexError('index out of bounds on list')
        if index == 0:
            self.prepend(value)
        elif index == self._length:
            self.append(value)
        else:
            new_node = _Node(value=value)
            prev = self._get_node_at(index - 1)
            new_node.next = prev.next
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
        if not curr or curr.value != value:
            raise ValueError('value not found')

        if prev:
            prev.next = curr.next
            if curr == self._tail:
                self._tail = prev
        else:
            self._head = self._head.next
            if self._head is None:
                self._tail = None
        self._length -= 1

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
        idx = self._get_positive_index(index)
        if idx < 0 or idx >= self._length:
            raise IndexError('invalid index')
        try:
            assert idx - 1 >= 0
            prev_node = self._get_node_at(idx - 1)
            value = prev_node.next.value
            prev_node.next = prev_node.next.next
            if prev_node.next is None:
                self._tail = prev_node
        except AssertionError:
            value = self._head.value
            self._head = self._head.next
            if self._head is None:
                self._tail = None
        self._length -= 1
        return value

    def clear(self) -> None:
        """Remove all elements from the list.

        Time complexity: O(1).
        """
        self._head = self._tail = None
        self._length = 0

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
        return self._tail.value if self._tail else None

    def find(self, value: T) -> int:
        """Return the index of the first occurrence of a value.

        Args:
            value: The value to search for.

        Returns:
            The index of the first occurrence of the value.

        Raises:
            ValueError: If the value is not found in the list.
        """
        for i, node_value in enumerate(self):
            if value == node_value:
                return i
        raise ValueError('value not found')

    def __len__(self) -> int:
        """Return the number of elements in the list.

        Returns:
            The number of elements in the linked list.
        """
        return self._length

    def __bool__(self) -> bool:
        """Return the truthiness of the list.

        Returns:
            False if the list is empty, True otherwise.
        """
        return self._length > 0

    def __getitem__(self, index: int) -> T:
        """Get the value at the given index.

        Args:
            index: 0-based index, negative indexes supported (Python style).

        Returns:
            The value at the specified index.

        Raises:
            IndexError: If the index is out of range.
        """
        return self._get_node_at(index).value

    def __setitem__(self, index: int, value: T) -> None:
        """Set item at the specified index.

        Args:
            index: The position at which to set the value.
                0-based index, negative indexes supported (Python style).
            value: The value to set.

        Raises:
            IndexError: If index is out of bounds.

        Time complexity: O(n).
        """
        self._get_node_at(index).value = value

    def __iter__(self) -> Iterator[T]:
        """Iterate through values in the list.

        Yields:
            The values in the list from head to tail.
        """
        curr = self._head
        while curr:
            yield curr.value
            curr = curr.next

    def __repr__(self) -> str:
        """Return a string representation of the linked list.

        Returns:
            A string representation showing the class name and list contents.
        """
        return f'{self.__class__.__name__}({list(self)})'

    def __str__(self) -> str:
        """Return a string representation of the linked list.

        Returns:
            A visual representation of the linked list.

        Time complexity: O(n).
        """
        if not self:
            return 'HEAD → TAIL'
        return 'HEAD → ' + ' → '.join(str(item) for item in self) + ' → TAIL'

    def _validate_index(self, index: int) -> None:
        """Validate that an index is within bounds.

        Args:
            index: The index to validate.

        Raises:
            IndexError: If the list is empty or index is out of bounds.
        """
        if self._length == 0:
            raise IndexError('empty list')
        if index < -self._length or index >= self._length:
            raise IndexError('index out-of-bounds')

    def _get_node_at(self, index: int) -> _Node[T]:
        """Get the node at the specified index.

        Args:
            index: The position of the node to retrieve. Supports negative indexing.

        Returns:
            The node at the specified index.

        Raises:
            IndexError: If the list is empty or index is out of bounds.

        Time complexity: O(n).
        """
        self._validate_index(index)
        index = self._get_positive_index(index)

        curr = self._head
        for _ in range(index):
            curr = curr.next
        return curr

    def _get_positive_index(self, index: int) -> int:
        """Convert a potentially negative index to a positive one.

        Args:
            index: The index to convert (may be negative).

        Returns:
            The positive equivalent of the index.
        """
        return self._length + index if index < 0 else index
