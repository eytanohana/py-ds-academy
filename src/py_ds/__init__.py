import importlib.metadata
import tomllib
from pathlib import Path

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
    pyproject_path = Path(__file__).parent.parent.parent / "pyproject.toml"
    with pyproject_path.open("rb") as f:
        pyproject = tomllib.load(f)
    package_name = pyproject["project"]["name"]
    try:
        return importlib.metadata.version(package_name)
    except importlib.metadata.PackageNotFoundError:
        # Fallback: read from pyproject.toml during development
        try:
            return pyproject["project"]["version"]
        except (FileNotFoundError, KeyError):
            return "0.0.0"


__version__ = _get_version()
