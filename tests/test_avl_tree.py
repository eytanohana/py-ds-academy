import random

import pytest

from py_ds.datastructures.trees.avl import AVLTree
from py_ds.datastructures.trees.base import _BinaryNode


def get_height(node: _BinaryNode | None) -> int:
    if node is None:
        return -1
    return 1 + max(get_height(node.left), get_height(node.right))


def is_balanced(node: _BinaryNode | None) -> bool:
    if node is None:
        return True

    left_height = get_height(node.left)
    right_height = get_height(node.right)

    if abs(left_height - right_height) > 1:
        return False

    return is_balanced(node.left) and is_balanced(node.right)


def validate_avl_tree(tree: AVLTree) -> None:
    # Check BST property
    values = list(tree.inorder())
    assert values == sorted(values), 'Tree violates BST property (inorder not sorted)'

    # Check AVL balance property
    assert is_balanced(tree._root), 'Tree is not balanced'


# --- Fixtures ---
@pytest.fixture
def small_avl() -> AVLTree[int]:
    # Inserting values
    values = [5, 3, 7, 2, 4, 6, 8]
    tree = AVLTree[int]()
    for v in values:
        tree.insert(v)
    return tree


# --- Tests ---


def test_avl_insert(small_avl: AVLTree[int]) -> None:
    assert len(small_avl) == 7
    assert list(small_avl.inorder()) == [2, 3, 4, 5, 6, 7, 8]
    validate_avl_tree(small_avl)


def test_avl_remove_leaf(small_avl: AVLTree[int]) -> None:
    # 2 is likely a leaf
    small_avl.remove(2)
    assert 2 not in small_avl
    assert len(small_avl) == 6
    assert list(small_avl.inorder()) == [3, 4, 5, 6, 7, 8]
    validate_avl_tree(small_avl)


def test_avl_remove_node_with_children(small_avl: AVLTree[int]) -> None:
    # 5 is the root
    small_avl.remove(5)
    assert 5 not in small_avl
    assert len(small_avl) == 6
    assert list(small_avl.inorder()) == [2, 3, 4, 6, 7, 8]
    validate_avl_tree(small_avl)


def test_avl_remove_non_existent(small_avl: AVLTree[int]) -> None:
    small_avl.remove(999)
    assert len(small_avl) == 7
    validate_avl_tree(small_avl)


def test_avl_rebalance_after_remove() -> None:
    # Construct a tree that will become unbalanced after removal
    #       20
    #     /    \
    #    10    30
    #            \
    #            40
    tree = AVLTree[int]()
    for v in [20, 10, 30, 40]:
        tree.insert(v)

    # Remove 10. Tree becomes right-heavy at 20.
    tree.remove(10)

    # Expect Left Rotation on 20
    # New root should be 30
    #       30
    #      /  \
    #    20    40

    assert list(tree.level_order()) == [30, 20, 40]
    assert list(tree.inorder()) == [20, 30, 40]
    validate_avl_tree(tree)


def test_left_left_case():
    """
    Left-Left Case (Right Rotation)
          30
         /             20
       20      ->     /  \
      /              10   30
    10
    """
    tree = AVLTree[int]()
    tree.insert(30)
    tree.insert(20)
    tree.insert(10)

    validate_avl_tree(tree)
    assert tree._root.value == 20
    assert tree._root.left.value == 10
    assert tree._root.right.value == 30


def test_right_right_case():
    """
    Right-Right Case (Left Rotation)
    10
      \                   20
       20       ->       /  \
         \             10    30
          30
    """
    tree = AVLTree[int]()
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)

    validate_avl_tree(tree)
    assert tree._root.value == 20
    assert tree._root.left.value == 10
    assert tree._root.right.value == 30


def test_left_right_case():
    """
    Left-Right Case (Left-Right Rotation)
       30
      /                20
    10        ->      /  \
      \             10    30
       20
    """
    tree = AVLTree[int]()
    tree.insert(30)
    tree.insert(10)
    tree.insert(20)

    validate_avl_tree(tree)
    assert tree._root.value == 20
    assert tree._root.left.value == 10
    assert tree._root.right.value == 30


def test_right_left_case():
    """
    Right-Left Case (Right-Left Rotation)
    10
      \               20
       30    ->      /  \
      /            10    30
    20
    """
    tree = AVLTree[int]()
    tree.insert(10)
    tree.insert(30)
    tree.insert(20)

    validate_avl_tree(tree)
    assert tree._root.value == 20
    assert tree._root.left.value == 10
    assert tree._root.right.value == 30


def test_large_random_insertions():
    # Use a fixed seed for reproducibility
    random.seed(42)
    tree = AVLTree[int]()
    values = list(range(100))
    random.shuffle(values)

    for v in values:
        tree.insert(v)
        # We can validate periodically or at end.
        # Validating at every step ensures rebalancing works incrementally.
        validate_avl_tree(tree)

    assert len(tree) == 100


def test_deletions_maintain_balance():
    random.seed(42)
    tree = AVLTree[int]()
    values = list(range(50))
    for v in values:
        tree.insert(v)

    random.shuffle(values)
    for v in values:
        tree.remove(v)
        validate_avl_tree(tree)

    assert len(tree) == 0
