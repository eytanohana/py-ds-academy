from importlib.metadata import PackageNotFoundError, version

from py_ds.datastructures.linked_list import DoublyLinkedList, SinglyLinkedList
from py_ds.datastructures.queue import Queue
from py_ds.datastructures.stack import Stack

__all__ = [
    "DoublyLinkedList",
    "Queue",
    "SinglyLinkedList",
    "Stack",
]


def _get_version() -> str:
    """Get version from installed package metadata."""
    try:
        return version("py-ds-academy")
    except PackageNotFoundError:
        return "0.0.0"


__version__ = _get_version()
