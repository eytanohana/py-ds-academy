import pytest

from py_ds.datastructures.heaps import MaxHeap


def test_new_heap_is_empty():
    heap = MaxHeap()
    assert len(heap) == 0
    assert not heap


def test_empty_heap_raises_on_peek():
    heap = MaxHeap()
    with pytest.raises(IndexError):
        heap.peek()


def test_empty_heap_raises_on_pop():
    heap = MaxHeap()
    with pytest.raises(IndexError):
        heap.pop()


def test_single_element_heap():
    heap = MaxHeap()
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


def test_init_with_iterable_builds_valid_max_heap():
    items = [5, 3, 8, 1, 4]
    heap = MaxHeap(items)

    # popping everything should give sorted order (descending)
    popped = [heap.pop() for _ in range(len(heap))]
    assert popped == sorted(items, reverse=True)

    assert len(heap) == 0
    assert not heap


def test_push_and_pop_maintains_max_order():
    heap = MaxHeap()

    values = [7, 2, 9, 1, 5, 3]
    for v in values:
        heap.push(v)

    popped = []
    while heap:
        popped.append(heap.pop())

    assert popped == sorted(values, reverse=True)


def test_mixed_push_pop_operations():
    heap = MaxHeap()

    heap.push(5)
    heap.push(2)
    heap.push(8)

    assert heap.pop() == 8  # largest so far

    heap.push(1)
    heap.push(3)

    # Now elements are {1, 2, 3, 5}
    assert heap.pop() == 5
    assert heap.pop() == 3

    heap.push(10)
    # Remaining elements are {1, 2, 10}
    assert heap.pop() == 10
    assert heap.pop() == 2
    assert heap.pop() == 1

    assert len(heap) == 0
    assert not heap


def test_heap_handles_duplicate_values():
    heap = MaxHeap()

    values = [5, 1, 3, 1, 2, 5, 1]
    for v in values:
        heap.push(v)

    popped = [heap.pop() for _ in range(len(heap))]

    assert popped == sorted(values, reverse=True)


def test_heap_supports_comparable_tuples():
    """
    Common priority-queue pattern: (priority, value) tuples.
    MaxHeap should use normal Python comparison, where tuples are ordered
    lexicographically. MaxHeap returns the tuple with the highest priority.
    """
    heap = MaxHeap()

    heap.push((3, 'low'))
    heap.push((1, 'high'))
    heap.push((2, 'medium'))

    assert heap.pop() == (3, 'low')
    assert heap.pop() == (2, 'medium')
    assert heap.pop() == (1, 'high')
    assert not heap


def test_peek_does_not_remove_element():
    heap = MaxHeap([4, 2, 7])

    first = heap.peek()
    second = heap.peek()

    # For a max heap, the largest element should be at the top
    assert first == second == 7
    # Size should not change after peek
    assert len(heap) == 3

    # But pop should remove it
    assert heap.pop() == 7
    assert len(heap) == 2
