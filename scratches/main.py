from py_ds import DoublyLinkedList, SinglyLinkedList

# Singly linked list
sll = SinglyLinkedList([1, 2, 3])
sll.append(4)
sll.prepend(0)
print(sll)
print(list(sll))  # [0, 1, 2, 3, 4]
print(SinglyLinkedList([]))

# Doubly linked list (more efficient append/prepend)
dll = DoublyLinkedList([1, 2, 3])
dll.append(4)  # O(1) operation
dll.prepend(0)  # O(1) operation
print(list(dll))  # [0, 1, 2, 3, 4]

# Reverse iteration (doubly linked only)
for item in dll.reverse_iter():
    print(item)  # Prints 4, 3, 2, 1, 0

print(dll)
print(DoublyLinkedList())
