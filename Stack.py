# Класс узла, содержащий данные и ссылку на следующий узел
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return f"Node('data'={self.data}, 'next_node'={self.next_node})"


# Инициализируется одним атрибутом, хранящим ссылку на верхний (крайний в стеке) узел.
class Stack:
    def __init__(self, top=None):
        self.top = top

    def __repr__(self):
        return f"Stack('top'={self.top})"

    def push(self, data):
        """Добавляет данные в стек"""
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node
