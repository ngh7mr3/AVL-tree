from unittest import TestCase
from tree import BinaryTree, TreeNode
from math import ceil, log
import numpy as np


class TestBalancedBinaryTree(TestCase):
    def __build_tree(self, nodes):
        for node in nodes:
            self.tree.add(node)

    def __test_tree_root_height(self, root, nodes_number):
        # Wiki formula
        self.assertTrue(root.height <= ceil(1.45 * log(nodes_number+2, 2)))

    def setUp(self):
        self.tree = BinaryTree()

    def test_init(self):
        self.assertIsNotNone(self.tree)
        self.assertTrue(self.tree.root is None)

    def test_root_node_specs(self):
        self.tree.add(1)
        self.assertTrue(isinstance(self.tree.root, TreeNode))
        self.assertEqual(self.tree.root.height, 0)
        self.assertEqual(self.tree.root.rst_height, 0)
        self.assertEqual(self.tree.root.lst_height, 0)

    def test_simple_balanced_triangle(self):
        test_arr = [1, 2, 3]
        self.__build_tree(test_arr)

        # Expecting the '2' to be the root because of balancing
        self.assertEqual(self.tree.root.data, 2)
        self.assertEqual(self.tree.root.left.data, 1)
        self.assertEqual(self.tree.root.right.data, 3)

        self.assertEqual(self.tree.root.height, 1)
        self.assertEqual(self.tree.root.lst_height, 1)
        self.assertEqual(self.tree.root.rst_height, 1)

    def test_tree_iterators(self):
        test_arr = np.arange(1, 10000)
        self.__build_tree(test_arr)

        for num, node in zip(test_arr, self.tree):
            self.assertEqual(node.data, num)

        for num, node in zip(test_arr[::-1], self.tree[::-1]):
            self.assertEqual(node.data, num)

    def test_balancing_on_equal_nodes(self):
        test_arr = [1, 2, 2, 2, 2]
        self.__build_tree(test_arr)

        for node in self.tree:
            self.assertTrue(-2 < node.balance < 2)

    def test_balancing_on_sorted_array(self):
        array_size = 10000
        test_arr = np.arange(1, array_size+1)
        self.__build_tree(test_arr)

        self.__test_tree_root_height(self.tree.root, array_size)
        for node in self.tree:
            self.assertTrue(-2 < node.balance < 2)

    def test_balancing_on_shuffled_array(self):
        array_size = 10000
        test_arr = np.arange(1, array_size+1)
        np.random.shuffle(test_arr)
        self.__build_tree(test_arr)

        self.__test_tree_root_height(self.tree.root, array_size)
        for node in self.tree:
            self.assertTrue(-2 < node.balance < 2)

