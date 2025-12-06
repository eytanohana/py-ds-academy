# test_minheap.py

import pytest
from py_ds.datastructures.heap import MinHeap


def test_new_heap_is_empty():
    heap = MinHeap()
    assert len(heap) == 0
    assert not heap


def test_empty_heap_raises_on_peek():
    heap = MinHeap()
    with pytest.raises(IndexError):
        heap.peek()


def test_empty_heap_raises_on_pop():
    heap = MinHeap()
    with pytest.raises(IndexError):
        heap.pop()


def test_single_element_heap():
    heap = MinHeap()
    heap.push(42)

    assert len(heap) == 1
    assert heap  # truthy

    assert heap.peek() == 42
    # peek should not remove the element
    assert len(heap) == 1

    value = heap.pop()
    assert value == 42
    assert len(heap) == 0
    assert not heap


def test_init_with_iterable_builds_valid_min_heap():
    items = [5, 3, 8, 1, 4]
    heap = MinHeap(items)

    # popping everything should give sorted order (ascending)
    popped = [heap.pop() for _ in range(len(heap))]
    assert popped == sorted(items)

    assert len(heap) == 0
    assert not heap


def test_push_and_pop_maintains_min_order():
    heap = MinHeap()

    values = [7, 2, 9, 1, 5, 3]
    for v in values:
        heap.push(v)

    popped = []
    while heap:
        popped.append(heap.pop())

    assert popped == sorted(values)


def test_mixed_push_pop_operations():
    heap = MinHeap()

    heap.push(5)
    heap.push(2)
    heap.push(8)

    assert heap.pop() == 2  # smallest so far

    heap.push(1)
    heap.push(3)

    # Now elements are {1, 3, 5, 8}
    assert heap.pop() == 1
    assert heap.pop() == 3

    heap.push(0)
    # Remaining elements are {0, 5, 8}
    assert heap.pop() == 0
    assert heap.pop() == 5
    assert heap.pop() == 8

    assert len(heap) == 0
    assert not heap


def test_heap_handles_duplicate_values():
    heap = MinHeap()

    values = [5, 1, 3, 1, 2, 5, 1]
    for v in values:
        heap.push(v)

    popped = [heap.pop() for _ in range(len(heap))]

    assert popped == sorted(values)


def test_heap_supports_comparable_tuples():
    """
    Common priority-queue pattern: (priority, value) tuples.
    MinHeap should use normal Python comparison, where tuples are ordered
    lexicographically (by priority, then by value).
    """
    heap = MinHeap()

    heap.push((3, "low"))
    heap.push((1, "high"))
    heap.push((2, "medium"))

    assert heap.pop() == (1, "high")
    assert heap.pop() == (2, "medium")
    assert heap.pop() == (3, "low")
    assert not heap


def test_peek_does_not_remove_element():
    heap = MinHeap([4, 2, 7])

    first = heap.peek()
    second = heap.peek()

    assert first == second == 2
    # Size should not change after peek
    assert len(heap) == 3

    # But pop should remove it
    assert heap.pop() == 2
    assert len(heap) == 2
