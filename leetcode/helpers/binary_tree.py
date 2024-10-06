# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def build_tree(array) -> Optional[TreeNode]:
    if not len(array):
        return None

    def set_node(index):
        if index >= len(array) or array[index] is None:
            return
        node = TreeNode(val=array[index])
        node.left = set_node(2*index+1)
        node.right = set_node(2*index+2)
        return node

    root = set_node(0)
    return root


if __name__ == "__main__":
    array = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
    root = build_tree(array)
    print(root.left.right.right.val)
