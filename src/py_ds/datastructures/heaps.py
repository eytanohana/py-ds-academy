from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import Generic, TypeVar

T = TypeVar('T')


class Heap(Generic[T], ABC):
    def __init__(self, items: Iterable[T] | None = None):
        items = items or []
        self._items: list[T] = []
        self._size: int = 0
        for item in items:
            self.push(item)

    def _swap(self, idx1, idx2) -> None:
        self._items[idx1], self._items[idx2] = self._items[idx2], self._items[idx1]

    @staticmethod
    def _left_index(index) -> int:
        return 2 * index + 1

    @staticmethod
    def _right_index(index) -> int:
        return 2 * index + 2

    def _has_left_child(self, index) -> bool:
        return self._left_index(index) < self._size

    def _has_right_child(self, index) -> bool:
        return self._right_index(index) < self._size

    def _left_child(self, index) -> T:
        return self._items[self._left_index(index)]

    def _right_child(self, index) -> T:
        return self._items[self._right_index(index)]

    @abstractmethod
    def _heapify_up(self) -> None: ...

    def push(self, item: T) -> None:
        index = self._size
        if index >= len(self._items):
            self._items.append(item)
        else:
            self._items[index] = item
        self._size += 1
        self._heapify_up()

    @abstractmethod
    def _heapify_down(self) -> None: ...

    def pop(self) -> T:
        if not self:
            raise IndexError('pop from an empty heap')
        item = self._items[0]
        self._items[0] = self._items[self._size - 1]
        self._size -= 1
        self._heapify_down()
        return item

    def peek(self) -> T:
        if not self:
            raise IndexError('peek from an empty heap')
        return self._items[0]

    def __len__(self) -> int:
        return self._size

    def __bool__(self) -> bool:
        return self._size > 0


class MinHeap(Heap):
    def _heapify_up(self) -> None:
        index = self._size - 1
        while index > 0 and self._items[index] < self._items[parent_idx := (index - 1) // 2]:
            self._swap(index, parent_idx)
            index = parent_idx

    def _heapify_down(self) -> None:
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
    def _heapify_up(self) -> None:
        index = self._size - 1
        while index > 0 and self._items[index] > self._items[parent_idx := (index - 1) // 2]:
            self._swap(index, parent_idx)
            index = parent_idx

    def _heapify_down(self) -> None:
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
