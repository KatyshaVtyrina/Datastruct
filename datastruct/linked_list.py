from datastruct.Node import Node


class LinkedList:
    """"Хранит ссылку на начало односвязного списка и на его конец, т.е. на первый и последний Node"""
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные и добавляет узел с этими данными в начало односвязного списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные и добавляет узел с этими данными в конец односвязного списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def print_ll_(self):
        """Вывод данных из односвязного списка:"""
        ll_string = ''
        node = self.head
        if node is None:
            return None
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string
