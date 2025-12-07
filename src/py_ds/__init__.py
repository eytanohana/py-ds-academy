from importlib.metadata import PackageNotFoundError, version

from py_ds.datastructures.heaps import MaxHeap, MinHeap
from py_ds.datastructures.linked_lists import DoublyLinkedList, SinglyLinkedList
from py_ds.datastructures.queue import Queue
from py_ds.datastructures.stack import Stack
from py_ds.datastructures.trees import BinarySearchTree

__all__ = [
    'BinarySearchTree',
    'DoublyLinkedList',
    'MaxHeap',
    'MinHeap',
    'Queue',
    'SinglyLinkedList',
    'Stack',
]


try:
    __version__ = version('py-ds-academy')
except PackageNotFoundError:
    __version__ = '0.0.0'
