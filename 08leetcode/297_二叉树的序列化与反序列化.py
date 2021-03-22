"""
297. 二叉树的序列化与反序列化
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。
"""
"""
方式1,序列化使用bfs
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


# 方式1
class Codec:
    @classmethod
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        results = []
        q = deque()
        if root:
            q.append(root)
        while q:
            node = q.popleft()
            if node:
                results.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                results.append("None")
        while results[-1] == "None":
            results.pop()
        return results

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data:
            q = deque(data)
            root = TreeNode(q.popleft())
        else:
            return None
        q2 = deque([root])
        while q:
            while q2:
                node = q2.popleft()
                if node:
                    if q:
                        node_val = q.popleft()

                        node_l = TreeNode(node_val) if node_val != "None" else None
                        node.left = node_l
                        q2.append(node_l)
                    else:
                        break
                    if q:
                        node_val = q.popleft()
                        node_r = TreeNode(node_val) if node_val != "None" else None
                        node.right = node_r
                        q2.append(node_r)
                    else:
                        break
        return root
