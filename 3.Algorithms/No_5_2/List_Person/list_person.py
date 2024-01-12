class Card:
    def __init__(self, data: str, prev=None, next=None) -> None:
        self.data = data
        self.prev = prev
        self.next = next


class ListPerson:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False

    def get_size(self) -> int:
        return self.size

    def add_tail(self, item) -> None:
        node = Card(item)
        if self.size == 0:
            self.head = node

        elif self.size > 0:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node
        self.size += 1

    def add_head(self, item) -> None:
        node = Card(item)
        if self.size == 0:
            self.tail = node

        elif self.size > 0:
            self.head.prev = node
            node.next = self.head

        self.head = node
        self.size += 1

    def add_index(self, item, index) -> None:
        if index < 0 or index > self.size:
            raise Exception('index out of range')

        if index == 0:
            self.add_head(item)
            return

        if index == self.size - 1:
            self.add_tail(item)
            return

        current = self.head
        current_index = 0

        while current:
            if current_index == index - 1:
                node = Card(item)
                node.prev = current
                node.next = current.next
                if current.next is not None:
                    current.next.prev = node
                current.next = node
                self.size += 1
                return
            current = current.next
            current_index += 1

    def add_after_family(self, item, family: str) -> None:
        if self.size == 0:
            raise Exception('List is avoid')

        count_similar = 0
        current = self.head

        while current:
            if current.data == family:
                count_similar += 1
                node = Card(item)
                node.next = current.next
                node.prev = current
                if current.next is not None:
                    current.next.prev = node
                current.next = node
                self.size += 1
                return
            current = current.next

        if count_similar == 0:
            raise Exception('List of persons does not contain this card')

    def pop_tail(self) -> str:
        if self.size == 0:
            raise Exception('list of person is avoid')

        data = self.tail.data
        if self.size == 1:
            self.tail = None
            self.head = None

        elif self.size > 1:
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -= 1
        return data

    def pop_head(self) -> str:
        if self.size == 0:
            raise Exception('list of person is avoid')

        data = self.head.data
        if self.size == 1:
            self.head = None
            self.tail = None

        elif self.size > 1:
            self.head = self.head.next
            self.head.prev = None

        self.size -= 1
        return data

    def pop_index(self, index) -> str:
        if self.size == 0:
            raise Exception('List of person is avoid')

        if index < 0 or index >= self.size:
            raise Exception('index out of range')

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

    def pop_family(self, family: str) -> str:
        if self.size == 0:
            raise Exception('List of person is avoid!')

        if self.size == 1:
            data = self.head.data
            self.head = None
            self.tail = None
            self.size -= 1
            return data

        count_similar = 0
        current = self.head

        while current:
            if current.data == family:
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
                count_similar += 1
                return data
            current = current.next

        if count_similar == 0:
            raise Exception('List of persons does not contain this card')
