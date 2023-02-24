import unittest

from datastruct.custom_queue import Queue


class TestQueue(unittest.TestCase):

    def test_repr_(self):
        self.assertEqual(Queue.__repr__(Queue()), "Queue('head'=None, 'tail'=None)")
        self.assertEqual(Queue.__repr__(Queue(5, 10)), "Queue('head'=5, 'tail'=10)")

    def test_enqueue(self):
        q = Queue()
        q.enqueue('data1')
        q.enqueue('data2')
        q.enqueue('data3')
        self.assertEqual(q.head.data, 'data1')
        self.assertEqual(q.head.next_node.data, 'data2')
        self.assertEqual(q.head.next_node.next_node.data, 'data3')
        self.assertEqual(q.tail.data, 'data3')
        self.assertEqual(q.tail.next_node, None)
