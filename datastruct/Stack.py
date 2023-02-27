from typing import Any
from datastruct.Node import Node


# Инициализируется одним атрибутом, хранящим ссылку на верхний (крайний в стеке) узел.
class Stack:
    def __init__(self, top=None):
        self.top = top

    def __repr__(self):
        return f"Stack('top'={self.top})"

    def push(self, data: Any) -> None:
        """Добавляет данные в стек"""
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self) -> Any:
        """Удаляет из стека верхний элемент (последний добавленный)"""
        pop_element = self.top
        self.top = self.top.next_node
        return pop_element.data
