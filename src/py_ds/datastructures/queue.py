from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import Generic, TypeVar

T = TypeVar('T')


class Queue(Generic[T]):
    """A simple FIFO (first-in, first-out) queue.

    Backed by a Python list, providing O(1) enqueue and O(1) dequeue operations.
    """

    def __init__(self, items: Iterable[T] | None = None) -> None:
        """Initialize the queue.

        Args:
            items: Optional iterable of initial items.
                   The first item of the iterable becomes the front of the queue.
        """
        self._items = list(items) if items else []

    # -------------------------------------------------
    # Core queue operations
    # -------------------------------------------------

    def enqueue(self, item: T) -> None:
        """Add an item to the back of the queue.

        Args:
            item: The item to add to the queue.

        Time complexity: O(1).
        """
        self._items.append(item)

    def dequeue(self) -> T:
        """Remove and return the front item of the queue.

        Returns:
            The item that was at the front of the queue.

        Raises:
            IndexError: If the queue is empty.

        Time complexity: O(1).
        """
        if self.is_empty():
            raise IndexError('dequeue from empty queue')
        return self._items.pop(0)

    def peek(self) -> T:
        """Return the front item without removing it.

        Returns:
            The item at the front of the queue.

        Raises:
            IndexError: If the queue is empty.

        Time complexity: O(1).
        """
        if self.is_empty():
            raise IndexError('peek from empty queue')
        return self._items[0]

    def is_empty(self) -> bool:
        """Check if the queue is empty.

        Returns:
            True if the queue contains no items, False otherwise.

        Time complexity: O(1).
        """
        return len(self._items) == 0

    # -------------------------------------------------
    # Bulk / utility operations
    # -------------------------------------------------

    def extend(self, items: Iterable[T]) -> None:
        """Enqueue multiple items in the order provided.

        The first item of the iterable becomes the next after the current back.

        Args:
            items: An iterable of items to enqueue.

        Time complexity: O(k), where k is the number of items.
        """
        for item in items:
            self.enqueue(item)

    def clear(self) -> None:
        """Remove all items from the queue.

        After this call, is_empty() returns True and len(queue) == 0.

        Time complexity: O(1).
        """
        self._items = []

    def to_list(self) -> list[T]:
        """Convert the queue to a Python list.

        Returns:
            A shallow copy of the queue contents as a list, ordered from
            front to back.

        Time complexity: O(n).
        """
        return self._items[::]

    # -------------------------------------------------
    # Python protocol methods
    # -------------------------------------------------

    def __len__(self) -> int:
        """Return the number of items in the queue.

        Returns:
            The number of items in the queue.

        Time complexity: O(1).
        """
        return len(self._items)

    def __bool__(self) -> bool:
        """Return the truthiness of the queue.

        Returns:
            False if the queue is empty, True otherwise.

        Enables: `if queue: ...`
        """
        return len(self._items) > 0

    def __iter__(self) -> Iterator[T]:
        """Iterate over the items in the queue from front to back.

        Yields:
            Each item in the queue, starting from the front.

        Example:
            q = Queue([1, 2, 3])
            list(q)  # [1, 2, 3]  (front to back)
        """
        return iter(self._items)

    def __repr__(self) -> str:
        """Return a string representation of the queue.

        Returns:
            A string representation showing the class name and queue contents.

        Example:
            Queue([1, 2, 3])
        """
        return f'Queue({self._items})'
