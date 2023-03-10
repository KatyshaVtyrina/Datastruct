from typing import Any

from datastruct.Stack import Node


class Queue:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def __repr__(self):
        return f"Queue('head'={self.head}, 'tail'={self.tail})"

    def enqueue(self, data: Any):
        """Добавляет данные в конец очереди"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self):
        """Удаляет из очереди крайний левый элемент (первый добавленный)"""
        if self.head is None:
            return None
        dequeue_element = self.head
        self.head = self.head.next_node
        return dequeue_element.data
