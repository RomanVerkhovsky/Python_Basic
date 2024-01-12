class Node:
    def __init__(self, data, prev=None) -> None:
        self.data = data
        self.prev = prev


class Stack:
    def __init__(self) -> None:
        self.top = None
        self.size = 0

    def push(self, item) -> None:
        """adding item in stack"""
        node = Node(item)
        node.prev = self.top
        self.top = node
        self.size += 1

    def pop(self) -> any:
        """deleting item from top stack"""
        if self.size == 0:
            raise Exception('stack is avoid')

        buff_data = self.top.data
        self.top = self.top.prev
        self.size -= 1
        return buff_data

    def peek(self) -> any:
        """returning item from top stack"""
        if self.size == 0:
            raise Exception('stack is avoid')
        return self.top.data

    def is_empty(self) -> bool:
        """checking for stack emptiness"""
        if self.size == 0:
            return True
        else:
            return False
