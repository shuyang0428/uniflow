import unittest
from uniflow.op.basic.expand_op import ExpandOp
from uniflow.node import Node


class TestExpandOp(unittest.TestCase):
    def setUp(self):
        # Set up a test node and ExpandOp instance before the test starts
        # Add a name argument to the Node instance
        self.test_node = Node(name="test_node", value_dict={"1": "2", "3": "4", "5": "6", "7": "8"})
        self.expand_op = ExpandOp(name="test_expand")

    def test_expand_op(self):
        # Process the node using ExpandOp
        expand_1, expand_2 = self.expand_op(self.test_node)

        # Check if the output matches the expected result
        expected_expand_1 = {"1": "2", "3": "4"}
        expected_expand_2 = {"5": "6", "7": "8"}
        self.assertEqual(expand_1.value_dict, expected_expand_1)
        self.assertEqual(expand_2.value_dict, expected_expand_2)
