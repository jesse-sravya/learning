from typing import List, Optional
from helpers.test_helper import TestHelper
from helpers.binary_tree import TreeNode, build_tree


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> List[int]:
            if not node:
                return []
            elif node.left is None and node.right is None:
                return [node.val]
            else:
                return dfs(node.left) + dfs(node.right)

        return dfs(root1) == dfs(root2)


TestHelper.test(
    Solution().leafSimilar(
        build_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]),
        build_tree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])),
    True)

TestHelper.test(
    Solution().leafSimilar(
        build_tree([1, 2, 3]),
        build_tree([1, 3, 2])),
    False)

TestHelper.test(
    Solution().leafSimilar(
        build_tree([1]),
        build_tree([1])),
    True)

TestHelper.test(
    Solution().leafSimilar(
        build_tree([1]),
        build_tree([2])),
    False)

TestHelper.test(
    Solution().leafSimilar(
        build_tree([1, 1, 4, 2, 3]),
        build_tree([1, 1, 1, 2, 3, 4])),
    True)
