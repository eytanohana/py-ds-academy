from importlib.metadata import PackageNotFoundError, packages_distributions, version

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
    """Get version from installed package metadata or pyproject.toml."""
    try:
        return version(packages_distributions()[__package__][0])
    except (PackageNotFoundError, KeyError):
        return "0.0.0"


__version__ = _get_version()
del _get_version
