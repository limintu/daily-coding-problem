import pytest
from solutions.common_data_type import TreeNode
from solutions.day_580 import Solution


TREE_1 = [10, 5, 5, None, 2, None, 1, None, None, None, None, None, None, -1]
TREE_2 = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1]


class TestSolution:
    def construct_tree(self, tree, node_index):
        if node_index + 1 <= len(tree) and tree[node_index] is not None:
            node = TreeNode(tree[node_index])
            node.left = self.construct_tree(tree, node_index * 2 + 1)
            node.right = self.construct_tree(tree, node_index * 2 + 2)

            return node

        return None

    @pytest.fixture()
    def solution(self):
        return Solution().find_minimum_path_sum

    def test_case_1(self, solution):
        root = self.construct_tree(TREE_1, 0)
        assert solution(root) == 15

    def test_case_2(self, solution):
        root = self.construct_tree(TREE_2, 0)
        assert solution(root) == 18
