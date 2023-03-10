import unittest

from datastruct.linked_list import LinkedList


class TestLinkedTest(unittest.TestCase):

    def setUp(self):
        """Данные для работы с тестом"""
        self.ll = LinkedList()

        self.ll2 = LinkedList()
        self.ll2.insert_beginning({'id': 1})
        self.ll2.insert_at_end({'id': 2})
        self.ll2.insert_at_end({'id': 3})
        self.ll2.insert_beginning({'id': 0})

    def test_empty_linked_list(self):
        """Про инициализации пустого односвязного списка """
        self.assertEqual(self.ll.head, None)
        self.assertEqual(self.ll.tail, None)
        self.assertEqual(self.ll.print_ll_(), None)

    def test_insert_beginning_element(self):
        """Ожидается добавление элемента в начало"""
        self.ll.insert_beginning({'id': 1})
        self.assertEqual(self.ll.head.data, {'id': 1})
        self.assertEqual(self.ll.tail.data, {'id': 1})
        self.assertEqual(self.ll.head.next_node, None)
        self.assertEqual(self.ll.tail.next_node, None)

    def test_insert_at_end_element(self):
        """Ожидается добавление элемента в конец"""
        self.ll.insert_at_end({'id': 1})
        self.assertEqual(self.ll.head.data, {'id': 1})
        self.assertEqual(self.ll.tail.data, {'id': 1})
        self.assertEqual(self.ll.head.next_node, None)
        self.assertEqual(self.ll.tail.next_node, None)

    def test_insert_incorrect_element(self):
        """Ожидается обработка исключения TypeError при добавлении некорректного элемента"""
        result = 'Данные не являются словарем или в словаре нет id.'
        self.assertEqual(self.ll.insert_beginning([1, 2, 3]), print(result))
        self.assertEqual(self.ll.insert_at_end({'one': 1}), print(result))

    def test_check_linked_list(self):
        """Проверяет правильность хранения ссылок"""
        self.assertEqual(self.ll2.head.data, {'id': 0})
        self.assertEqual(self.ll2.tail.data, {'id': 3})
        self.assertEqual(self.ll2.head.next_node.data, {'id': 1})
        self.assertEqual(self.ll2.head.next_node.next_node.data, {'id': 2})
        self.assertEqual(self.ll2.head.next_node.next_node.next_node.data, {'id': 3})
        self.assertEqual(self.ll2.tail.next_node, None)

    def test_print_ll(self):
        """Ожидаются все данные односвязного списка"""
        self.assertEqual(self.ll2.print_ll_(), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")

    def test_to_list(self):
        """Ожидается list с данными односвязного списка"""
        self.assertEqual(self.ll.to_list(), None)
        self.assertIsInstance(self.ll2.to_list(), list)

    def test_get_data_by_id(self):
        """Ожидается получение первого найденного словаря по переданному значению"""
        self.assertEqual(self.ll2.get_data_by_id(3), {'id': 3})
        self.assertEqual(self.ll2.get_data_by_id(4), None)
