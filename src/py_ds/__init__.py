from importlib.metadata import PackageNotFoundError, version

from py_ds.datastructures.heaps import MaxHeap, MinHeap
from py_ds.datastructures.linked_lists import DoublyLinkedList, LinkedList
from py_ds.datastructures.queue import Queue
from py_ds.datastructures.stack import Stack
from py_ds.datastructures.trees import AVLTree, BinarySearchTree

__all__ = [
    'AVLTree',
    'BinarySearchTree',
    'DoublyLinkedList',
    'LinkedList',
    'MaxHeap',
    'MinHeap',
    'Queue',
    'Stack',
]


try:
    __version__ = version('py-ds-academy')
except PackageNotFoundError:
    __version__ = '0.0.0'
