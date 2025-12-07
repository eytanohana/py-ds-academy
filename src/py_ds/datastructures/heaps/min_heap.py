from py_ds.datastructures.heaps.base import Heap


class MinHeap(Heap):
    def _heapify_up(self) -> None:
        index = self._size - 1
        while index > 0 and self._items[index] < self._items[parent_idx := (index - 1) // 2]:
            self._swap(index, parent_idx)
            index = parent_idx

    def _heapify_down(self) -> None:
        parent_idx = 0
        while self._has_left_child(parent_idx):
            smaller_child, smaller_child_idx = self._left_child(parent_idx), self._left_index(parent_idx)
            if self._has_right_child(parent_idx) and (right_child := self._right_child(parent_idx)) < smaller_child:
                smaller_child, smaller_child_idx = right_child, self._right_index(parent_idx)

            if self._items[parent_idx] > smaller_child:
                self._swap(parent_idx, smaller_child_idx)
                parent_idx = smaller_child_idx
            else:
                break
