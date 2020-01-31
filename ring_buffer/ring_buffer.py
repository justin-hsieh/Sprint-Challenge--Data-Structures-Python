from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        
        # if storage is not at capacity
        if self.storage.length < self.capacity:
            # Add item and assign it as tail
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        
        # if at capacity
        else:
            # if pointing to tail, reassign to head
            if self.current == self.storage.tail:
                self.current = self.storage.head
            # if not pointing to tail, point to next value for assignment
            else:
                self.current = self.current.next
            # Replace existing value with item value
            self.current.value = item


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # Point to head of storage
        current = self.storage.head

        # Assuming None is not present, otherwise do for loop with if/else statement
        while current is not None:
            # Append values
            list_buffer_contents.append(current.value)
            # Move to next node
            current = current.next

        return list_buffer_contents






# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
