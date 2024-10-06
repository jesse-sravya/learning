from typing import Optional
from helpers.binary_tree import TreeNode, build_tree
from helpers.test_helper import TestHelper


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        return (
            (root.val if root.val >= low and root.val <= high else 0) +
            self.rangeSumBST(root.left, low, high) +
            self.rangeSumBST(root.right, low, high)
        )


TestHelper.test(Solution().rangeSumBST(
    build_tree([10, 5, 15, 3, 7, None, 18]), 7, 15), 32)
TestHelper.test(Solution().rangeSumBST(
    build_tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6]), 6, 10), 23)
