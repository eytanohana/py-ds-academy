import pytest

from py_ds.datastructures.linked_lists.singly_linked import SinglyLinkedList


def test_empty_list_initial_state():
    ll: SinglyLinkedList[int] = SinglyLinkedList()
    assert len(ll) == 0
    assert ll.to_list() == []
    assert ll.head() is None
    assert ll.tail() is None
    assert bool(ll) is False


def test_init_with_items():
    ll = SinglyLinkedList([1, 2, 3])
    assert len(ll) == 3
    ll_list = ll.to_list()
    assert ll_list == [1, 2, 3]
    assert ll.head() == 1
    assert ll.tail() == 3


def test_append_adds_to_end():
    ll = SinglyLinkedList[int]()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.to_list() == [1, 2, 3]
    assert ll.tail() == 3
    assert len(ll) == 3


def test_prepend_adds_to_front():
    ll = SinglyLinkedList[int]()
    ll.prepend(3)
    ll.prepend(2)
    ll.prepend(1)
    assert ll.to_list() == [1, 2, 3]
    assert ll.head() == 1
    assert len(ll) == 3


def test_insert_at_beginning_middle_and_end():
    ll = SinglyLinkedList([1, 3, 4])

    # insert at beginning
    ll.insert(0, 0)
    assert ll.to_list() == [0, 1, 3, 4]

    # insert in middle
    ll.insert(2, 2)
    assert ll.to_list() == [0, 1, 2, 3, 4]

    # insert at end (index == len)
    ll.insert(len(ll), 5)
    assert ll.to_list() == [0, 1, 2, 3, 4, 5]


def test_insert_out_of_bounds_raises():
    ll = SinglyLinkedList([1, 2, 3])
    with pytest.raises(IndexError):
        ll.insert(10, 99)
    with pytest.raises(IndexError):
        ll.insert(-4, 99)


def test_insert_negative_index():
    ll = SinglyLinkedList([1, 2, 3])
    ll.insert(-2, 99)
    assert ll.to_list() == [1, 99, 2, 3]

    ll.insert(-1, 55)
    assert ll.to_list() == [1, 99, 2, 55, 3]


def test_remove_existing_value():
    ll = SinglyLinkedList([1, 2, 3, 2])

    ll.remove(2)  # remove first occurrence
    assert ll.to_list() == [1, 3, 2]

    ll.remove(2)
    assert ll.to_list() == [1, 3]

    ll.remove(1)
    assert ll.to_list() == [3]

    ll.remove(3)
    assert ll.to_list() == []
    assert len(ll) == 0


def test_remove_nonexistent_raises():
    ll = SinglyLinkedList([1, 2, 3])
    with pytest.raises(ValueError):
        ll.remove(99)


def test_pop_default_pops_last():
    ll = SinglyLinkedList([1, 2, 3])
    value = ll.pop()
    assert value == 3


def test_pop_positive_index():
    ll = SinglyLinkedList([1, 2, 3, 4, 5])
    value = ll.pop(0)
    assert value == 1
    assert ll.to_list() == [2, 3, 4, 5]

    value = ll.pop(3)
    assert value == 5
    assert ll.to_list() == [2, 3, 4]

    value = ll.pop(1)
    assert value == 3
    assert ll.to_list() == [2, 4]


def test_pop_negative_index():
    ll = SinglyLinkedList([1, 2, 3, 4, 5])
    value = ll.pop(-2)
    assert value == 4
    assert ll.to_list() == [1, 2, 3, 5]

    value = ll.pop(-4)
    assert value == 1
    assert ll.to_list() == [2, 3, 5]

    value = ll.pop(-2)
    assert value == 3
    assert ll.to_list() == [2, 5]


def test_str_and_repr():
    ll = SinglyLinkedList([1, 2, 3])
    assert str(ll) == 'HEAD → 1 → 2 → 3 → NULL'
    assert repr(ll) == 'SinglyLinkedList([1, 2, 3])'

    ll2 = SinglyLinkedList()
    assert str(ll2) == 'HEAD → NULL'
    assert repr(ll2) == 'SinglyLinkedList([])'


def test_get_item():
    ll = SinglyLinkedList([1, 2, 3])
    assert ll[0] == 1
    assert ll[1] == 2
    assert ll[2] == 3
    with pytest.raises(IndexError):
        _ = ll[3]

    assert ll[-1] == 3
    assert ll[-2] == 2
    assert ll[-3] == 1
    with pytest.raises(IndexError):
        _ = ll[-4]
