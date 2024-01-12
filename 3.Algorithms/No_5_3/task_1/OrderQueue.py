class Order:
    def __init__(self, ID: int, price: float, prev=None) -> None:
        self.__ID = ID
        self.__price = price
        self.prev = prev

    def get_ID(self) -> int:
        return self.__ID

    def get_price(self) -> float:
        return self.__price

    def get_prev_order(self) -> any:
        return self.prev

    def set_ID(self, new_ID: int) -> None:
        self.__ID = new_ID

    def set_price(self, new_price: float) -> None:
        self.__price = new_price


class OrderQueue:
    """a class for managing orders (uses a queue)"""
    def __init__(self) -> None:
        self.__head = None
        self.__tail = None
        self.__size = 0

    def get_head(self) -> any:
        return self.__head

    def get_tail(self) -> any:
        return self.__tail

    def get_size(self) -> int:
        return self.__size

    def is_empty(self) -> bool:
        """checking for queue emptiness"""
        if self.__size == 0:
            return True
        return False

    def waiting_orders_count(self) -> int:
        """returns the number of orders awaiting service"""
        return self.__size

    def place_order(self, ID: int, price: float) -> None:
        """adding an order to the queue"""
        order = Order(ID, price)
        if self.__size == 0:
            self.__head = order
        else:
            self.__tail.prev = order
        self.__tail = order
        self.__size += 1

    def serve_order(self) -> any:
        """deletes and returns the first order from the queue for service"""
        if self.__size == 0:
            raise ValueError('Queue of orders is empty')

        order = self.__head

        if self.__size == 1:
            self.__head = None
            self.__tail = None
        else:
            self.__head = self.__head.prev

        return order

    def peek_next_order(self) -> any:
        """returns the first order from the queue without deleting it"""
        if self.__size == 0:
            raise ValueError('Queue of orders is empty')

        return self.__head
