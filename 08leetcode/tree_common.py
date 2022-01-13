class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque
# 方式1

def serialize(root):
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

def deserialize( data):
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
