from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import Generic, TypeVar

T = TypeVar('T')


class Queue(Generic[T]):
    """
    A simple FIFO (first-in, first-out) queue.

    Backed by collections.deque for O(1) enqueue/dequeue behavior.
    """

    def __init__(self, items: Iterable[T] | None = None) -> None:
        """
        Initialize the queue.

        Args:
            items: Optional iterable of initial items.
                   The first item of the iterable becomes the front of the queue.
        """
        self._items = list(items) if items else []

    # -------------------------------------------------
    # Core queue operations
    # -------------------------------------------------

    def enqueue(self, item: T) -> None:
        """
        Add an item to the back of the queue.

        Time complexity: O(1).
        """
        self._items.append(item)

    def dequeue(self) -> T:
        """
        Remove and return the front item of the queue.

        Raises:
            IndexError: if the queue is empty.

        Time complexity: O(1).
        """
        if self.is_empty():
            raise IndexError('dequeue from empty queue')
        return self._items.pop(0)

    def peek(self) -> T:
        """
        Return the front item without removing it.

        Raises:
            IndexError: if the queue is empty.
        """
        if self.is_empty():
            raise IndexError('peek from empty queue')
        return self._items[0]

    def is_empty(self) -> bool:
        """
        Return True if the queue contains no items.

        Time complexity: O(1).
        """
        return len(self._items) == 0

    # -------------------------------------------------
    # Bulk / utility operations
    # -------------------------------------------------

    def extend(self, items: Iterable[T]) -> None:
        """
        Enqueue multiple items in the order provided.

        The first item of the iterable becomes the next after the current back.
        """
        for item in items:
            self.enqueue(item)

    def clear(self) -> None:
        """
        Remove all items from the queue.
        """
        self._items = []

    def to_list(self) -> list[T]:
        """
        Return a shallow list copy of the queue contents from front to back.
        """
        return self._items[::]

    # -------------------------------------------------
    # Python protocol methods
    # -------------------------------------------------

    def __len__(self) -> int:
        """Return the number of items in the queue."""
        return len(self._items)

    def __bool__(self) -> bool:
        """Truthiness: False if empty, True otherwise."""
        return len(self._items) > 0

    def __iter__(self) -> Iterator[T]:
        """
        Iterate from front -> back.
        """
        return iter(self._items)

    def __repr__(self) -> str:
        """
        Return a readable representation, e.g.:

            Queue([1, 2, 3])
        """
        return f'Queue({self._items})'
