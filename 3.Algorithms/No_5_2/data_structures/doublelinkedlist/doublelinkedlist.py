class Node:
    def __init__(self, data, prev=None, next=None) -> None:
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self) -> bool:
        """checking for list emptiness"""
        if self.size == 0:
            return True
        else:
            return False

    def get_size(self) -> int:
        """determining the number of list items"""
        return self.size

    def add(self, item) -> None:
        """adding an item to the end of the list"""
        node = Node(item)
        if self.size == 0:
            self.head = node

        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node
        self.size += 1

    def add_head(self, item) -> None:
        """adding an item to the top of the list"""
        node = Node(item)
        if self.size == 0:
            self.tail = node

        elif self.size > 0:
            node.next = self.head
            self.head.prev = node

        self.head = node
        self.size += 1

    def insert(self, item, index) -> None:
        """adding an item by index"""
        if index < 0 or index > self.size:
            raise IndexError('index out of range')

        if index == 0:
            self.add_head(item)
            return

        current = self.head
        current_index = 0

        while current:
            if current_index == index - 1:
                node = Node(item)
                node.prev = current
                node.next = current.next
                if current.next is not None:
                    current.next.prev = node
                current.next = node
                self.size += 1
                return
            current = current.next
            current_index += 1

    def pop(self) -> any:
        """removing an element from the end"""
        if self.size == 0:
            raise Exception('list is avoid')

        data = self.tail.data
        if self.size == 1:
            self.head = None
            self.tail = None

        elif self.size > 1:
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -= 1
        return data

    def pop_head(self) -> any:
        """removing an element from the top"""
        if self.size == 0:
            raise Exception('list is avoid')

        data = self.head.data
        if self.size == 1:
            self.head = None
            self.tail = None

        elif self.size > 1:
            self.head = self.head.next
            self.head.prev = None

        self.size -= 1
        return data

    def pop_index(self, index) -> any:
        """removing an element by index"""
        if self.size == 0:
            raise Exception('list is avoid')

        if index < 0 or index >= self.size:
            raise Exception('list is avoid')

        if self.size == 1:
            data = self.head.data
            self.head = None
            self.tail = None
            self.size -= 1
            return data

        current = self.head
        current_index = 0

        while current:
            if current_index == index:
                data = current.data
                if current.prev is not None:
                    current.prev.next = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                if current.prev is None:
                    self.head = current.next
                if current.next is None:
                    self.tail = current.prev
                self.size -= 1
                return data
            current = current.next
            current_index += 1


a = DoublyLinkedList()

