import unittest
from Stack import Node, Stack


class TestNode(unittest.TestCase):

    def test__repr__(self):
        self.assertEqual(Node.__repr__(Node(5)), "Node('data'=5, 'next_node'=None)")
        self.assertEqual(Node.__repr__(Node('a', 'b')), "Node('data'=a, 'next_node'=b)")


class TestStack(unittest.TestCase):

    def test__repr__(self):
        self.assertEqual(Stack.__repr__(Stack()), "Stack('top'=None)")
        self.assertEqual(Stack.__repr__(Stack(5)), "Stack('top'=5)")

    def test_push(self):
        s = Stack()
        s.push('data1')
        s.push('data2')
        self.assertEqual(s.top.data, 'data2')
        self.assertEqual(s.top.next_node.data, 'data1')
        self.assertEqual(s.top.next_node.next_node, None)

    def test_pop(self):
        s = Stack()
        s.push('data1')
        s.push('data2')
        data = s.pop()
        self.assertEqual(s.top.data, 'data1')
        self.assertEqual(data, 'data2')
        data = s.pop()
        self.assertEqual(s.top, None)
        self.assertEqual(data, 'data1')
