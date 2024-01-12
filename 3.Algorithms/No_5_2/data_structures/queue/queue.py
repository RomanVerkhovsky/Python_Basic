class Node:
    def __init__(self, data, prev=None) -> None:
        self.data = data
        self.prev = prev


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self) -> bool:
        """checking for queue emptiness"""
        if self.size == 0:
            return True
        else:
            return False

    def enqueue(self, item) -> None:
        """adding item in end of queue"""
        node = Node(item)
        if self.size == 0:
            self.head = node
        else:
            self.tail.prev = node
        self.tail = node
        self.size += 1

    def dequeue(self) -> any:
        """deleting item from top queue"""
        if self.size == 0:
            return None

        buff_data = self.head.data

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.prev

        return buff_data

    def peek(self) -> any:
        """returning data from top queue"""
        if self.size == 0:
            return None
        return self.head.data
