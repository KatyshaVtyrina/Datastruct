import unittest

from datastruct.custom_queue import Queue


class TestQueue(unittest.TestCase):

    def test_repr_(self):
        """Ожидается инициализация очереди"""
        self.assertEqual(Queue.__repr__(Queue()), "Queue('head'=None, 'tail'=None)")
        self.assertEqual(Queue.__repr__(Queue(5, 10)), "Queue('head'=5, 'tail'=10)")

    def test_enqueue(self):
        """Ожидается добавление элемента в конец очереди"""
        q = Queue()
        q.enqueue('data1')
        q.enqueue('data2')
        q.enqueue('data3')
        self.assertEqual(q.head.data, 'data1')
        self.assertEqual(q.head.next_node.data, 'data2')
        self.assertEqual(q.head.next_node.next_node.data, 'data3')
        self.assertEqual(q.tail.data, 'data3')
        self.assertEqual(q.tail.next_node, None)

    def test_dequeue(self):
        """Ожидается удаление первого элемента из очереди"""
        q = Queue()
        q.enqueue('data1')
        q.enqueue('data2')
        q.enqueue('data3')
        self.assertEqual(q.dequeue(), 'data1')
        self.assertEqual(q.dequeue(), 'data2')
        self.assertEqual(q.dequeue(), 'data3')
        self.assertEqual(q.dequeue(), None)
