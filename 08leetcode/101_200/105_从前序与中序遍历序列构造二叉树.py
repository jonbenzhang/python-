"""
105. 从前序与中序遍历序列构造二叉树
根据一棵树的前序遍历与中序遍历构造二叉树。
注意:
你可以假设树中没有重复的元素。
例如，给出
前序遍历 preorder = [3,9,6,20,15,7]
中序遍历 inorder = [6,9,3,15,20,7]
"""
from tree_common import serialize
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None
            # 前序遍历的第一个节点就是根节点
            root = TreeNode(preorder[pre_left])
            root_index = in_index[root.val]
            # 相对于当前数组的索引
            b = root_index - in_left
            root_l = build(pre_left + 1, pre_left + b, in_left, in_left + b - 1)
            root_r = build(pre_left + b + 1, pre_right, in_left + b + 1, in_right)
            root.left = root_l
            root.right = root_r
            return root

        in_index = {val: i for i, val in enumerate(inorder)}
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)


if __name__ == '__main__':
    print(serialize(Solution.buildTree([1, 2, 3], [3, 2, 1])))
