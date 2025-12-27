from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import Generic, TypeVar

T = TypeVar('T')


class Stack(Generic[T]):
    """A simple LIFO (last-in, first-out) stack.

    Backed by a dynamic array (Python list). Provides efficient O(1) operations
    for push, pop, and peek operations.
    """

    def __init__(self, items: Iterable[T] | None = None) -> None:
        """Initialize the stack.

        Args:
            items: Optional iterable of initial items. The last item in the
                   iterable should be considered the "top" of the stack.

        Example:
            Stack([1, 2, 3])  # 3 is at the top
        """
        self._items = list(items) if items else []

    # -------- Core stack operations --------

    def push(self, item: T) -> None:
        """Push a single item onto the top of the stack.

        Args:
            item: The item to push onto the stack.

        Time complexity: O(1) amortized.
        """
        self._items.append(item)

    def pop(self) -> T:
        """Remove and return the top item of the stack.

        Returns:
            The item that was at the top of the stack.

        Raises:
            IndexError: If the stack is empty.

        Time complexity: O(1).
        """
        if self.is_empty():
            raise IndexError('pop from empty stack')
        return self._items.pop()

    def peek(self) -> T:
        """Return the top item of the stack without removing it.

        Returns:
            The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.

        Time complexity: O(1).
        """
        if self.is_empty():
            raise IndexError('peek from empty stack')
        return self._items[-1]

    def is_empty(self) -> bool:
        """Check if the stack is empty.

        Returns:
            True if the stack has no elements, False otherwise.

        Time complexity: O(1).
        """
        return len(self._items) == 0

    # -------- Bulk / utility operations --------

    def clear(self) -> None:
        """Remove all items from the stack.

        After this call, is_empty() returns True and len(stack) == 0.

        Time complexity: O(1).
        """
        self._items = []

    def extend(self, items: Iterable[T]) -> None:
        """Push multiple items onto the stack, in iteration order.

        The last item of `items` becomes the new top of the stack.

        Args:
            items: An iterable of items to push onto the stack.

        Example:
            s = Stack([1])
            s.extend([2, 3])
            # now stack top is 3

        Time complexity: O(k), where k is the number of items.
        """
        for item in items:
            self.push(item)

    def to_list(self) -> list[T]:
        """Convert the stack to a Python list.

        Returns:
            A shallow copy of the stack contents as a list. The last element
            of the returned list is the top of the stack.

        Time complexity: O(n).
        """
        return self._items[::]

    # -------- Python protocol methods --------

    def __len__(self) -> int:
        """Return the number of items in the stack.

        Returns:
            The number of items in the stack.

        Time complexity: O(1).
        """
        return len(self._items)

    def __bool__(self) -> bool:
        """Return the truthiness of the stack.

        Returns:
            False if the stack is empty, True otherwise.

        Enables: `if stack: ...`
        """
        return len(self._items) > 0

    def __iter__(self) -> Iterator[T]:
        """Iterate over the items in the stack from top to bottom.

        Yields:
            Each item in the stack, starting from the top.

        Example:
            s = Stack([1, 2, 3])
            list(s)  # [3, 2, 1]  (top to bottom)
        """
        return iter(self._items[::-1])

    def __repr__(self) -> str:
        """Return a string representation of the stack.

        Returns:
            A string representation showing the class name and stack contents.

        Example:
            Stack([1, 2, 3])
        """
        return f'Stack({self.to_list()})'
