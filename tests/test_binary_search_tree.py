import pytest

from py_ds.datastructures.trees.binary_search_tree import BinarySearchTree

# ------------------------------------------------------------
# Fixtures
# ------------------------------------------------------------


@pytest.fixture
def empty_bst() -> BinarySearchTree[int]:
    return BinarySearchTree()


@pytest.fixture
def small_bst() -> BinarySearchTree[int]:
    # Inserting in this order should create an unbalanced tree in many
    # implementations, but we only care about the resulting behavior,
    # not the exact shape.
    values = [5, 3, 7, 2, 4, 6, 8]
    return BinarySearchTree(values)


# ------------------------------------------------------------
# Empty tree behavior
# ------------------------------------------------------------


def test_empty_tree_properties(empty_bst: BinarySearchTree[int]) -> None:
    assert empty_bst.is_empty
    assert len(empty_bst) == 0
    assert empty_bst.height == -1

    # Traversals over an empty tree yield no elements
    assert list(empty_bst.inorder()) == []
    assert list(empty_bst.preorder()) == []
    assert list(empty_bst.postorder()) == []
    assert list(empty_bst.level_order()) == []

    # Contains must be False for any value
    assert 42 not in empty_bst

    # min / max must fail on empty trees
    with pytest.raises(ValueError):
        empty_bst.min()
    with pytest.raises(ValueError):
        empty_bst.max()


# ------------------------------------------------------------
# Basic insertion and membership
# ------------------------------------------------------------


def test_single_insert_updates_properties(empty_bst: BinarySearchTree[int]) -> None:
    empty_bst.insert(10)

    assert not empty_bst.is_empty
    assert len(empty_bst) == 1
    assert 10 in empty_bst
    assert 5 not in empty_bst

    # Height of a single-node tree is 0
    assert empty_bst.height == 0

    # All traversals of a single-node tree should yield [10]
    expected = [10]
    assert list(empty_bst.inorder()) == expected
    assert list(empty_bst.preorder()) == expected
    assert list(empty_bst.postorder()) == expected
    assert list(empty_bst.level_order()) == expected

    assert empty_bst.min() == 10
    assert empty_bst.max() == 10


def test_multiple_inserts_and_len() -> None:
    bst = BinarySearchTree[int]()
    values = [5, 2, 8, 1, 3, 7, 9]

    for v in values:
        bst.insert(v)

    assert len(bst) == len(values)
    for v in values:
        assert v in bst

    # Some values that were not inserted
    for v in [0, 4, 6, 10]:
        assert v not in bst


# ------------------------------------------------------------
# Ordering invariant (inorder traversal must be sorted)
# ------------------------------------------------------------


def test_inorder_traversal_is_sorted(small_bst: BinarySearchTree[int]) -> None:
    values = [5, 3, 7, 2, 4, 6, 8]
    inorder_values = list(small_bst.inorder())

    assert inorder_values == sorted(values)


def test_preorder_and_postorder_have_correct_length(
    small_bst: BinarySearchTree[int],
) -> None:
    n = len(small_bst)

    assert len(list(small_bst.preorder())) == n
    assert len(list(small_bst.postorder())) == n
    assert len(list(small_bst.level_order())) == n

    # Using sets, we can at least validate they contain the same elements
    # (not their order).
    elements = {5, 3, 7, 2, 4, 6, 8}
    assert set(small_bst.inorder()) == elements
    assert set(small_bst.preorder()) == elements
    assert set(small_bst.postorder()) == elements
    assert set(small_bst.level_order()) == elements


# ------------------------------------------------------------
# min / max operations
# ------------------------------------------------------------


def test_min_and_max_on_non_empty_tree(small_bst: BinarySearchTree[int]) -> None:
    assert small_bst.min() == 2
    assert small_bst.max() == 8


def test_min_and_max_after_insertions() -> None:
    bst = BinarySearchTree[int]()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(1)

    assert bst.min() == 1
    assert bst.max() == 15


# ------------------------------------------------------------
# Removal behavior
# ------------------------------------------------------------


def test_remove_from_single_node_tree() -> None:
    bst = BinarySearchTree[int]()
    bst.insert(10)

    bst.remove(10)

    assert bst.is_empty
    assert len(bst) == 0
    assert 10 not in bst
    assert list(bst.inorder()) == []


def test_remove_leaf_node(small_bst: BinarySearchTree[int]) -> None:
    # small_bst contains [2, 3, 4, 5, 6, 7, 8] in inorder
    original_len = len(small_bst)

    # 2 is a leaf in many standard BST shapes for this insertion pattern;
    # but we don't depend on shape for correctness, only on the final invariants.
    small_bst.remove(2)

    assert len(small_bst) == original_len - 1
    assert 2 not in small_bst
    assert list(small_bst.inorder()) == [3, 4, 5, 6, 7, 8]
    # Still a valid BST: inorder must remain sorted
    assert list(small_bst.inorder()) == sorted(list(small_bst.inorder()))


def test_remove_node_with_one_child() -> None:
    # Build a tree where a known node has exactly one child.
    bst = BinarySearchTree[int]()
    for v in [5, 3, 7, 6]:
        bst.insert(v)

    # In many standard shapes, 7 has a single left child 6.
    bst.remove(7)

    # 7 is gone, but 6 should still be in the tree.
    assert 7 not in bst
    assert 6 in bst

    inorder_values = list(bst.inorder())
    assert inorder_values == sorted(inorder_values)


def test_remove_node_with_two_children() -> None:
    bst = BinarySearchTree[int]()
    values = [5, 3, 7, 2, 4, 6, 8]
    for v in values:
        bst.insert(v)

    # 5 has two children (3, 7) with subtrees.
    bst.remove(5)

    # 5 is removed
    assert 5 not in bst

    # Remaining values should be original minus 5
    remaining = sorted(v for v in values if v != 5)
    inorder_values = list(bst.inorder())
    assert inorder_values == remaining

    # BST property still holds: inorder must be sorted
    assert inorder_values == sorted(inorder_values)


def test_remove_non_existent_value_is_noop(small_bst: BinarySearchTree[int]) -> None:
    original_len = len(small_bst)
    original_inorder = list(small_bst.inorder())

    small_bst.remove(999)  # value not in tree

    assert len(small_bst) == original_len
    assert list(small_bst.inorder()) == original_inorder


# ------------------------------------------------------------
# Height sanity checks (not strict balancing)
# ------------------------------------------------------------


def test_height_after_insertions_unbalanced() -> None:
    bst = BinarySearchTree[int]()
    # Insert values in sorted order to create a worst-case skewed tree
    for v in [1, 2, 3, 4, 5]:
        bst.insert(v)

    # In a naive BST, height should be length - 1 in this pattern
    # (degenerate linked-list shape)
    assert len(bst) == 5
    assert bst.height >= 4  # allow for more clever implementations, just not < 4


def test_height_on_small_balanced_pattern(small_bst: BinarySearchTree[int]) -> None:
    # We don't enforce exact height, but we can at least assert it's not absurd.
    # For 7 nodes, the minimal possible height is 2 (perfectly balanced).
    h = small_bst.height
    assert h >= 2
    assert h < len(small_bst)  # height must always be < number of nodes


# ------------------------------------------------------------
# Clearing the tree
# ------------------------------------------------------------


def test_clear_resets_tree(small_bst: BinarySearchTree[int]) -> None:
    small_bst.clear()

    assert small_bst.is_empty
    assert len(small_bst) == 0
    assert list(small_bst.inorder()) == []
    assert list(small_bst.preorder()) == []
    assert list(small_bst.postorder()) == []
    assert list(small_bst.level_order()) == []

    with pytest.raises(ValueError):
        small_bst.min()
    with pytest.raises(ValueError):
        small_bst.max()
