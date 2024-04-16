"""深度优先遍历

前序，中序，后序遍历, 通常基于递归实现 TODO 基于迭代实现
"""

res_pre = []
res_in = []
res_post = []


class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


def pre_order(root: TreeNode | None):
    """前序遍历 根节点->左子树->右子树"""
    if root is None:
        return
    res_pre.append(root.val)
    pre_order(root.left)
    pre_order(root.right)


def in_order(root: TreeNode | None):
    """中序遍历 左子树->根节点->右子树"""
    if root is None:
        return
    in_order(root.left)
    res_in.append(root.val)
    in_order(root.right)


def post_order(root: TreeNode | None):
    """后序遍历 左子树->右子树->根节点"""
    if root is None:
        return
    in_order(root.left)
    in_order(root.right)
    res_post.append(root.val)
