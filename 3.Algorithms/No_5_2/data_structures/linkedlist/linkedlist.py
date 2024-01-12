class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None
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
        if self.size == 0:
            self.head = Node(item)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(item)

        self.size += 1

    def add_head(self, item) -> None:
        """adding an item to the top of the list"""
        node = Node(item)
        node.next = self.head
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

        while current is not None:
            if current_index == index - 1:
                node = Node(item)
                node.next = current.next
                current.next = node
                self.size += 1
                return
            current = current.next
            current_index += 1

    def insert_value(self, item: any, value: any) -> None:
        """adding an element(item) after a given value"""
        current = self.head
        count_even = 0
        while current:
            if current.data == value:
                node = Node(item)
                node.next = current.next
                current.next = node
                count_even += 1
                self.size += 1
                return
            current = current.next

        if count_even == 0:
            raise ValueError('list do not contain value')

    def pop(self) -> any:
        """removing an element from the end"""
        if self.size == 0:
            raise IndexError('pop from empty list')

        if self.size == 1:
            data = self.head.data
            self.head = None
            self.size -= 1
            return data

        pre_current = None
        current = self.head
        while current.next is not None:
            pre_current = current
            current = current.next
        data = current.data
        pre_current.next = None
        self.size -= 1
        return data

    def pop_head(self) -> any:
        """removing an element from the top"""
        if self.size == 0:
            raise IndexError('pop from empty list')

        if self.size == 1:
            data = self.head.data
            self.head = None
            self.size -= 1
            return data

        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def pop_index(self, index: int) -> any:
        """removing an element by index"""
        if self.size == 0:
            raise IndexError('pop from empty list')

        if index < 0 or index >= self.size:
            raise IndexError('index out of range')

        if self.size == 1:
            data = self.head.data
            self.head = None
            self.size -= 1
            return data

        if index == 0:
            return self.pop_head()

        if index + 1 == self.size:
            return self.pop()

        current = self.head
        current_index = 0

        while current:
            if current_index == index - 1:
                data = current.data
                current.next = current.next.next
                self.size -= 1
                return data

            current = current.next
            current_index += 1

    def pop_value(self, value: any) -> any:
        """removing an element by value"""
        if self.size == 0:
            raise IndexError('pop from empty list')

        count_even = 0
        pre_current = None
        current = self.head
        while current is not None:
            if current.data == value:
                count_even += 1
                data = current.data
                if pre_current is None:
                    return self.pop_head()
                pre_current.next = current.next
                self.size -= 1
                return data

            pre_current = current
            current = current.next

        if count_even == 0:
            raise ValueError('list do not contain value')

    def peek_index(self, index) -> any:
        """return item by index"""
        if self.size == 0:
            raise IndexError('list is empty')

        if index < 0 or index >= self.size:
            raise IndexError('index out of range')

        current = self.head
        current_index = 0
        while current_index != index:
            current_index += 1
            current = current.next

        return current.data


lst = LinkedList()
for i in range(3):
    lst.add(i + 1)

lst_head = lst.head
while lst_head:
    print(lst_head.data)
    lst_head = lst_head.next

print('size =', lst.size)

print('')

print('peek = ', lst.peek_index(2))
print('')

lst_head = lst.head
while lst_head:
    print(lst_head.data)
    lst_head = lst_head.next

print('size =', lst.size)


