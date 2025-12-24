"""Tests for DoublyLinkedList."""

import pytest

from py_ds.datastructures.linked_lists.doubly_linked import DoublyLinkedList


def test_empty_list_initial_state():
    """Empty list should have length 0, no head/tail."""
    dll = DoublyLinkedList()
    assert len(dll) == 0
    assert dll.head() is None
    assert dll.tail() is None
    assert bool(dll) is False


def test_init_with_items():
    """Should be able to initialize with an iterable."""
    dll = DoublyLinkedList([1, 2, 3])
    assert len(dll) == 3
    assert dll.head() == 1
    assert dll.tail() == 3


def test_append_adds_to_end():
    """Append should add items to the end."""
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    assert list(dll) == [1, 2, 3]
    assert dll.head() == 1
    assert dll.tail() == 3
    assert len(dll) == 3


def test_append_is_o1():
    """Append should be O(1) with tail pointer."""
    dll = DoublyLinkedList()
    # Just verify it works with many elements
    for i in range(100):
        dll.append(i)
    assert len(dll) == 100
    assert dll.tail() == 99


def test_prepend_adds_to_front():
    """Prepend should add items to the beginning."""
    dll = DoublyLinkedList()
    dll.prepend(3)
    dll.prepend(2)
    dll.prepend(1)
    assert list(dll) == [1, 2, 3]
    assert dll.head() == 1
    assert dll.tail() == 3
    assert len(dll) == 3


def test_insert_at_beginning_middle_and_end():
    """Insert should handle insertion at any position."""
    dll = DoublyLinkedList([1, 2, 4, 5])

    # Insert at beginning
    dll.insert(0, 0)
    assert list(dll) == [0, 1, 2, 4, 5]

    # Insert in middle
    dll.insert(3, 3)
    assert list(dll) == [0, 1, 2, 3, 4, 5]

    # Insert at end
    dll.insert(6, 6)
    assert list(dll) == [0, 1, 2, 3, 4, 5, 6]

    dll.insert(-1, 7)
    assert list(dll) == [0, 1, 2, 3, 4, 5, 7, 6]


def test_insert_out_of_bounds_raises():
    """Insert should raise IndexError for invalid indices."""
    dll = DoublyLinkedList([1, 2])
    with pytest.raises(IndexError):
        dll.insert(-10, 0)
    with pytest.raises(IndexError):
        dll.insert(10, 0)


def test_remove_existing_value():
    """Remove should remove the first occurrence of a value."""
    dll = DoublyLinkedList([1, 2, 3, 2, 4])
    dll.remove(2)
    assert list(dll) == [1, 3, 2, 4]
    dll.remove(1)
    assert list(dll) == [3, 2, 4]
    dll.remove(4)
    assert list(dll) == [3, 2]
    dll.remove(2)
    assert list(dll) == [3]
    dll.remove(3)
    assert list(dll) == []


def test_remove_nonexistent_raises():
    """Remove should raise ValueError if value not found."""
    dll = DoublyLinkedList([1, 2, 3])
    with pytest.raises(ValueError, match='value not found'):
        dll.remove(10)


def test_pop_default_pops_last():
    """Pop with no argument should remove and return the last element."""
    dll = DoublyLinkedList([1, 2, 3])
    value = dll.pop()
    assert value == 3
    assert list(dll) == [1, 2]
    value = dll.pop()
    assert value == 2
    assert list(dll) == [1]
    value = dll.pop()
    assert value == 1
    assert list(dll) == []


def test_pop_at_index():
    """Pop should remove and return element at specified index."""
    dll = DoublyLinkedList([1, 2, 3, 4, 5])

    # Pop first
    assert dll.pop(0) == 1
    assert list(dll) == [2, 3, 4, 5]

    # Pop middle
    assert dll.pop(2) == 4
    assert list(dll) == [2, 3, 5]

    # Pop last
    assert dll.pop(-1) == 5
    assert list(dll) == [2, 3]


def test_pop_empty_raises():
    """Pop should raise IndexError on empty list."""
    dll = DoublyLinkedList()
    with pytest.raises(IndexError):
        dll.pop()


def test_find():
    """Find should return the index of the first occurrence."""
    dll = DoublyLinkedList([1, 2, 3, 2, 4])
    assert dll.find(1) == 0
    assert dll.find(2) == 1
    assert dll.find(4) == 4


def test_find_nonexistent_raises():
    """Find should raise ValueError if value not found."""
    dll = DoublyLinkedList([1, 2, 3])
    with pytest.raises(ValueError, match='value not found'):
        dll.find(10)


def test_clear():
    """Clear should remove all elements."""
    dll = DoublyLinkedList([1, 2, 3, 4, 5])
    dll.clear()
    assert len(dll) == 0
    assert dll.head() is None
    assert dll.tail() is None
    assert list(dll) == []


def test_iteration():
    """Should be able to iterate through the list."""
    dll = DoublyLinkedList([1, 2, 3, 4, 5])
    result = [x for x in dll]
    assert result == [1, 2, 3, 4, 5]


def test_reverse_iteration():
    """DoublyLinkedList should support reverse iteration."""
    dll = DoublyLinkedList([1, 2, 3, 4, 5])
    result = [x for x in dll.reverse_iter()]
    assert result == [5, 4, 3, 2, 1]


def test_reverse_iteration_empty():
    """Reverse iteration on empty list should work."""
    dll = DoublyLinkedList()
    result = [x for x in dll.reverse_iter()]
    assert result == []


def test_indexing():
    """Should support __getitem__ for indexing."""
    dll = DoublyLinkedList([10, 20, 30, 40])
    assert dll[0] == 10
    assert dll[1] == 20
    assert dll[2] == 30
    assert dll[3] == 40
    assert dll[-1] == 40
    assert dll[-2] == 30
    assert dll[-3] == 20
    assert dll[-4] == 10


def test_indexing_out_of_bounds():
    """Indexing should raise IndexError for invalid indices."""
    dll = DoublyLinkedList([1, 2, 3])
    with pytest.raises(IndexError):
        _ = dll[10]
    with pytest.raises(IndexError):
        _ = dll[-5]  # Negative indices not supported


def test_setitem():
    """Should support __setitem__ for assignment."""
    dll = DoublyLinkedList([1, 2, 3])
    dll[0] = 10
    dll[2] = 30
    assert list(dll) == [10, 2, 30]
    dll[-1] = 40
    assert list(dll) == [10, 2, 40]


def test_setitem_out_of_bounds():
    """Setting item should raise IndexError for invalid indices."""
    dll = DoublyLinkedList([1, 2, 3])
    with pytest.raises(IndexError):
        dll[10] = 999


def test_str_and_repr():
    """Repr should show the list contents."""
    dll = DoublyLinkedList([1, 2, 3])
    assert str(dll) == 'HEAD ⇆ 1 ⇆ 2 ⇆ 3 ⇆ TAIL'
    assert repr(dll) == 'DoublyLinkedList([1, 2, 3])'

    dll2 = DoublyLinkedList()
    assert str(dll2) == 'HEAD ⇆ TAIL'
    assert repr(dll2) == 'DoublyLinkedList([])'


def test_bool():
    """Empty list is falsy, non-empty is truthy."""
    dll = DoublyLinkedList()
    assert not dll
    dll.append(1)
    assert dll


def test_complex_operations():
    """Test a sequence of mixed operations."""
    dll = DoublyLinkedList()

    # Build up
    dll.append(2)
    dll.prepend(1)
    dll.append(3)
    dll.insert(3, 4)
    assert list(dll) == [1, 2, 3, 4]

    # Modify
    dll[1] = 20
    assert list(dll) == [1, 20, 3, 4]

    # Remove
    dll.remove(20)
    assert list(dll) == [1, 3, 4]

    # Pop
    assert dll.pop(1) == 3
    assert list(dll) == [1, 4]

    # Clear
    dll.clear()
    assert len(dll) == 0
