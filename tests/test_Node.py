import unittest
from datastruct.Node import Node


class TestNode(unittest.TestCase):

    def test_get_node(self):
        """Ожидается инициализация узла"""
        self.assertEqual(Node.__repr__(Node(5)), "Node('data'=5, 'next_node'=None)")
        self.assertEqual(Node.__repr__(Node('a', 'b')), "Node('data'=a, 'next_node'=b)")
