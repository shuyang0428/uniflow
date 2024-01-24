import unittest
from uniflow.op.basic.expand_op import ExpandOp
from uniflow.node import Node


class TestExpandOp(unittest.TestCase):
    def setUp(self):
        # 在测试开始前设置好测试用的节点和 ExpandOp 实例
        self.test_node = Node(value_dict={"1": "2", "3": "4", "5": "6", "7": "8"})
        self.expand_op = ExpandOp(name="test_expand")

    def test_expand_op(self):
        # 使用 ExpandOp 处理节点
        expand_1, expand_2 = self.expand_op(self.test_node)

        # 检查输出是否符合预期
        expected_expand_1 = {"1": "2", "3": "4"}
        expected_expand_2 = {"5": "6", "7": "8"}
        self.assertEqual(expand_1.value_dict, expected_expand_1)
        self.assertEqual(expand_2.value_dict, expected_expand_2)
