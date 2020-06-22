"""
This question was asked by Apple.

Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

   10
  /  \
 5    5
  \    \
   2    1
       /
      1
"""
from solutions.common_data_type import TreeNode


class Solution:
    def find_minimum_path_sum(self, root: TreeNode) -> int:
        if not root:
            return 0

        if root.left and root.right:
            return root.val + min(self.find_minimum_path_sum(root.left),
                                  self.find_minimum_path_sum(root.right))
        elif root.left:
            return root.val + self.find_minimum_path_sum(root.left)
        elif root.right:
            return root.val + self.find_minimum_path_sum(root.right)
        else:
            return root.val
