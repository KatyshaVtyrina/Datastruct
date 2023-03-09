from datastruct.Node import Node


class LinkedList:
    """"Хранит ссылку на начало односвязного списка и на его конец, т.е. на первый и последний Node"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные и добавляет узел с этими данными в начало односвязного списка"""
        check_data = self.check_data(data)
        if check_data is not None:
            new_node = Node(check_data)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next_node = self.head
                self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные и добавляет узел с этими данными в конец односвязного списка"""
        check_data = self.check_data(data)
        if check_data is not None:
            new_node = Node(check_data)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next_node = new_node
                self.tail = new_node

    @staticmethod
    def check_data(data):
        """Проверяет, что данные это словарь, который содержит ключ ['id]"""
        try:
            if not isinstance(data, dict):
                raise TypeError
            else:
                if 'id' not in list(data.keys()):
                    raise TypeError
        except TypeError:
            print('Данные не являются словарем или в словаре нет id.')
        else:
            return data

    def print_ll_(self):
        """Вывод данных из односвязного списка"""
        ll_string = ''
        node = self.head
        if node is None:
            return None
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def to_list(self):
        """Возвращает список словарей односвязного списка"""
        ll_list = []
        node = self.head
        if node is None:
            return None
        while node:
            ll_list.append(node.data)
            node = node.next_node
        return ll_list

    def get_data_by_id(self, value):
        """Возвращает первый найденный в LinkedList словарь с ключом id,
        значение которого равно переданному в метод значению"""
        try:
            ll_list = self.to_list()
            for item in ll_list:
                if item['id'] == value:
                    return item
            raise ValueError
        except ValueError:
            return None
