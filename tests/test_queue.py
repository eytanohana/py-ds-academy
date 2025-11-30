import pytest

from py_ds.datastructures.queue import Queue


def test_empty_queue_initial_state():
    q: Queue[int] = Queue()
    assert q.is_empty() is True
    assert len(q) == 0
    assert bool(q) is False


def test_init_with_items():
    q = Queue([1, 2, 3])
    assert len(q) == 3
    assert q.peek() == 1  # front of the queue
    assert q.to_list() == [1, 2, 3]


def test_enqueue_increases_size_and_changes_back():
    q = Queue[int]()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    assert len(q) == 3
    assert q.peek() == 10  # front remains same
    assert q.to_list() == [10, 20, 30]


def test_dequeue_returns_items_in_fifo_order():
    q = Queue([1, 2, 3])
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.is_empty() is True


def test_dequeue_on_empty_queue_raises():
    q = Queue[int]()
    with pytest.raises(IndexError):
        q.dequeue()


def test_peek_does_not_remove():
    q = Queue([1, 2])
    assert q.peek() == 1
    assert len(q) == 2  # remains same
    assert q.to_list() == [1, 2]


def test_peek_on_empty_raises():
    q = Queue[int]()
    with pytest.raises(IndexError):
        q.peek()


def test_extend_adds_items_in_order():
    q = Queue([1])
    q.extend([2, 3, 4])
    assert q.to_list() == [1, 2, 3, 4]
    assert q.peek() == 1
    assert len(q) == 4


def test_clear_empties_queue():
    q = Queue([1, 2, 3])
    q.clear()
    assert q.is_empty() is True
    assert len(q) == 0
    assert q.to_list() == []


def test_iteration_front_to_back():
    q = Queue([1, 2, 3])
    assert list(q) == [1, 2, 3]


def test_bool_truthiness():
    assert bool(Queue()) is False
    assert bool(Queue([1])) is True


def test_repr():
    q = Queue([1, 2, 3])
    assert repr(q) == "Queue([1, 2, 3])"
