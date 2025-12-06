from collections.abc import Iterable
from typing import Generic, TypeVar

T = TypeVar("T")


class MinHeap(Generic[T]):
    def __init__(self, items: Iterable[T] | None = None):
        items = items or []
        self._size = 0
        for item in items:
            self.push(item)

    def push(self, item: T) -> None: ...

    def pop(self) -> T: ...

    def peek(self) -> T: ...

    def __len__(self) -> int:
        return self._size

    def __bool__(self) -> bool:
        return self._size > 0
