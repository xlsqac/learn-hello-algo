"""
二叉树遍历
层序遍历，广度优先
O(n)
借助队列实现
"""
from collections import deque


class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


def level_order(root: TreeNode | None) -> list[int]:
    queue: deque[TreeNode] = deque()
    queue.append(root)
    res = []
    while queue:
        node: TreeNode = queue.popleft()
        res.append(node.val)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return res


if __name__ == '__main__':
    # 初始化节点
    n1 = TreeNode(val=1)
    n2 = TreeNode(val=2)
    n3 = TreeNode(val=3)
    n4 = TreeNode(val=4)
    n5 = TreeNode(val=5)
    # 构建节点之间的应用
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5

    print(level_order(n1))
