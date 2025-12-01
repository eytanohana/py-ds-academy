from py_ds.datastructures.linked_list import DoublyLinkedList, SinglyLinkedList
from py_ds.datastructures.queue import Queue
from py_ds.datastructures.stack import Stack

import importlib.metadata

__all__ = [
    "DoublyLinkedList",
    "Queue",
    "SinglyLinkedList",
    "Stack",
]


try:
    __version__ = importlib.metadata.version(__name__)
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0"

print(__version__)
