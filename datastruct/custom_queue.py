from typing import Any

from datastruct.Stack import Node


class Queue:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def __repr__(self):
        return f"Queue('head'={self.head}, 'tail'={self.tail})"

    def enqueue(self, data: Any):
        """Добавляет данные в очередь"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
