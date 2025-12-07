import pytest

from py_ds.datastructures.stack import Stack


def test_empty_stack_initial_state():
    s: Stack[int] = Stack()
    assert s.is_empty() is True
    assert len(s) == 0
    assert bool(s) is False


def test_init_with_items():
    s = Stack([1, 2, 3])
    assert len(s) == 3
    assert s.peek() == 3
    assert s.to_list() == [1, 2, 3]


def test_push_increases_size_and_changes_top():
    s = Stack[int]()
    s.push(10)
    s.push(20)
    assert len(s) == 2
    assert s.peek() == 20
    assert s.to_list() == [10, 20]


def test_pop_returns_items_in_lifo_order():
    s = Stack([1, 2, 3])
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty() is True


def test_pop_on_empty_stack_raises():
    s = Stack[int]()
    with pytest.raises(IndexError):
        s.pop()


def test_peek_does_not_remove():
    s = Stack([1, 2])
    assert s.peek() == 2
    assert len(s) == 2  # still intact


def test_peek_on_empty_raises():
    s = Stack[int]()
    with pytest.raises(IndexError):
        s.peek()


def test_extend_pushes_items_in_correct_order():
    s = Stack([1])
    s.extend([2, 3, 4])
    assert s.peek() == 4
    assert s.to_list() == [1, 2, 3, 4]


def test_clear_removes_all_items():
    s = Stack([1, 2, 3])
    s.clear()
    assert s.is_empty() is True
    assert len(s) == 0
    assert s.to_list() == []


def test_iteration_bottom_to_top():
    # Assuming your __iter__ yields top -> bottom
    s = Stack([1, 2, 3])
    assert list(s) == [3, 2, 1]


def test_bool_truthiness():
    assert bool(Stack()) is False
    assert bool(Stack([1])) is True


def test_repr_contains_items():
    s = Stack([1, 2, 3])
    assert repr(s) == 'Stack([1, 2, 3])'
