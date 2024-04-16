"""
二叉树
"""


class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


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
    # 插入和删除结点
    p = TreeNode(0)
    n1.left = p
    p.left = n2
    n1.left = n2
