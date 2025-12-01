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
        print(__package__)
        dist_name = packages_distributions()[__package__][0]
        print(dist_name)
        vers = version(dist_name)
        return vers
    except PackageNotFoundError:
        # Fallback: read from pyproject.toml during development
        return "0.0.0"


__version__ = _get_version()
