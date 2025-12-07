from collections.abc import Iterable
from typing import Generic, TypeVar

T = TypeVar('T')


class MinHeap(Generic[T]):
    def __init__(self, items: Iterable[T] | None = None):
        items = items or []
        self._items: list[T] = []
        self._size: int = 0
        for item in items:
            self.push(item)

    def _swap(self, idx1, idx2) -> None:
        self._items[idx1], self._items[idx2] = self._items[idx2], self._items[idx1]

    def push(self, item: T) -> None:
        index = self._size
        if index >= len(self._items):
            self._items.append(item)
        else:
            self._items[index] = item
        while index > 0 and self._items[index] < self._items[parent_idx := (index - 1) // 2]:
            self._swap(index, parent_idx)
            index = parent_idx
        self._size += 1

    def pop(self) -> T: ...

    def peek(self) -> T:
        if not self:
            raise IndexError('peek from an empty heap')
        return self._items[0]

    def __len__(self) -> int:
        return self._size

    def __bool__(self) -> bool:
        return self._size > 0
