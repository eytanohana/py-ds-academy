from typing import Iterable, Generic, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self, items: Iterable[T] | None = None) -> None:
        if items is not None:
            self.items = list(items)[::-1]
        self.items = []
