from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import Generic, TypeVar

T = TypeVar('T')


class Heap(Generic[T], ABC):
    """Abstract base class for heap data structures.

    A heap is a complete binary tree that satisfies the heap property.
    This base class provides common functionality for both min and max heaps.
    """

    def __init__(self, items: Iterable[T] | None = None):
        """Initialize the heap with optional items.

        Args:
            items: Optional iterable of items to initialize the heap with.
                If None, creates an empty heap.
        """
        items = items or []
        self._items: list[T] = []
        self._size: int = 0
        for item in items:
            self.push(item)

    def _swap(self, idx1, idx2) -> None:
        """Swap two elements in the heap array.

        Args:
            idx1: Index of the first element.
            idx2: Index of the second element.
        """
        self._items[idx1], self._items[idx2] = self._items[idx2], self._items[idx1]

    @staticmethod
    def _left_index(index) -> int:
        """Calculate the left child index of a node.

        Args:
            index: The index of the parent node.

        Returns:
            The index of the left child node.
        """
        return 2 * index + 1

    @staticmethod
    def _right_index(index) -> int:
        """Calculate the right child index of a node.

        Args:
            index: The index of the parent node.

        Returns:
            The index of the right child node.
        """
        return 2 * index + 2

    def _has_left_child(self, index) -> bool:
        """Check if a node has a left child.

        Args:
            index: The index of the node to check.

        Returns:
            True if the node has a left child, False otherwise.
        """
        return self._left_index(index) < self._size

    def _has_right_child(self, index) -> bool:
        """Check if a node has a right child.

        Args:
            index: The index of the node to check.

        Returns:
            True if the node has a right child, False otherwise.
        """
        return self._right_index(index) < self._size

    def _left_child(self, index) -> T:
        """Get the left child value of a node.

        Args:
            index: The index of the parent node.

        Returns:
            The value of the left child node.

        Raises:
            IndexError: If the node does not have a left child.
        """
        return self._items[self._left_index(index)]

    def _right_child(self, index) -> T:
        """Get the right child value of a node.

        Args:
            index: The index of the parent node.

        Returns:
            The value of the right child node.

        Raises:
            IndexError: If the node does not have a right child.
        """
        return self._items[self._right_index(index)]

    @abstractmethod
    def _heapify_up(self) -> None:
        """Restore heap property by moving the last element up the tree.

        This method is called after inserting a new element to maintain
        the heap property. Implementation depends on whether it's a min
        or max heap.
        """
        ...

    def push(self, item: T) -> None:
        """Add an item to the heap.

        Args:
            item: The item to add to the heap.

        Time complexity: O(log n) where n is the number of elements.
        """
        index = self._size
        if index >= len(self._items):
            self._items.append(item)
        else:
            self._items[index] = item
        self._size += 1
        self._heapify_up()

    @abstractmethod
    def _heapify_down(self) -> None:
        """Restore heap property by moving the root element down the tree.

        This method is called after removing the root element to maintain
        the heap property. Implementation depends on whether it's a min
        or max heap.
        """
        ...

    def pop(self) -> T:
        """Remove and return the root element of the heap.

        Returns:
            The root element of the heap (minimum for MinHeap, maximum for MaxHeap).

        Raises:
            IndexError: If the heap is empty.

        Time complexity: O(log n) where n is the number of elements.
        """
        if not self:
            raise IndexError('pop from an empty heap')
        item = self._items[0]
        self._items[0] = self._items[self._size - 1]
        self._size -= 1
        self._heapify_down()
        return item

    def peek(self) -> T:
        """Return the root element without removing it.

        Returns:
            The root element of the heap (minimum for MinHeap, maximum for MaxHeap).

        Raises:
            IndexError: If the heap is empty.

        Time complexity: O(1).
        """
        if not self:
            raise IndexError('peek from an empty heap')
        return self._items[0]

    def __len__(self) -> int:
        """Return the number of elements in the heap.

        Returns:
            The number of elements in the heap.

        Time complexity: O(1).
        """
        return self._size

    def __bool__(self) -> bool:
        """Return the truthiness of the heap.

        Returns:
            False if the heap is empty, True otherwise.

        Enables: `if heap: ...`
        """
        return self._size > 0


class MinHeap(Heap):
    """A min-heap implementation.

    In a min-heap, the parent node is always less than or equal to its children.
    The root element is the minimum value in the heap.
    """

    def _heapify_up(self) -> None:
        """Restore min-heap property by moving the last element up.

        Compares the newly inserted element with its parent and swaps if
        the parent is larger, continuing up the tree until the heap property
        is restored.
        """
        index = self._size - 1
        while index > 0 and self._items[index] < self._items[parent_idx := (index - 1) // 2]:
            self._swap(index, parent_idx)
            index = parent_idx

    def _heapify_down(self) -> None:
        """Restore min-heap property by moving the root element down.

        Compares the root with its children and swaps with the smaller child
        if the root is larger, continuing down the tree until the heap property
        is restored.
        """
        parent_idx = 0
        while self._has_left_child(parent_idx):
            smaller_child, smaller_child_idx = self._left_child(parent_idx), self._left_index(parent_idx)
            if self._has_right_child(parent_idx) and (right_child := self._right_child(parent_idx)) < smaller_child:
                smaller_child, smaller_child_idx = right_child, self._right_index(parent_idx)

            if self._items[parent_idx] > smaller_child:
                self._swap(parent_idx, smaller_child_idx)
                parent_idx = smaller_child_idx
            else:
                break


class MaxHeap(Heap):
    """A max-heap implementation.

    In a max-heap, the parent node is always greater than or equal to its children.
    The root element is the maximum value in the heap.
    """

    def _heapify_up(self) -> None:
        """Restore max-heap property by moving the last element up.

        Compares the newly inserted element with its parent and swaps if
        the parent is smaller, continuing up the tree until the heap property
        is restored.
        """
        index = self._size - 1
        while index > 0 and self._items[index] > self._items[parent_idx := (index - 1) // 2]:
            self._swap(index, parent_idx)
            index = parent_idx

    def _heapify_down(self) -> None:
        """Restore max-heap property by moving the root element down.

        Compares the root with its children and swaps with the larger child
        if the root is smaller, continuing down the tree until the heap property
        is restored.
        """
        parent_idx = 0
        while self._has_left_child(parent_idx):
            bigger_child, bigger_child_idx = self._left_child(parent_idx), self._left_index(parent_idx)
            if self._has_right_child(parent_idx) and (right_child := self._right_child(parent_idx)) > bigger_child:
                bigger_child, bigger_child_idx = right_child, self._right_index(parent_idx)

            if self._items[parent_idx] < bigger_child:
                self._swap(parent_idx, bigger_child_idx)
                parent_idx = bigger_child_idx
            else:
                break
