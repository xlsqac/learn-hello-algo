"""
链表创建以及操作
"""


class ListNode:
    def __init__(self, value: int):
        self.value: int = value
        self.next: ListNode | None = None


def insert(before_node: ListNode, node: ListNode):
    """
    插入结点，只需更改指针. O(1)
    :param before_node: 插入到哪个结点之后
    :param node: 要插入的结点
    :return:
    """
    node.next = before_node.next
    before_node.next = node


def delete(node: ListNode):
    """
    删除传入结点的下一个结点。O(1)
    :param node:
    :return:
    """
    if node.next is None:
        return
    node.next = node.next.next


def access(head: ListNode, index: int) -> ListNode | None:
    """
    访问结点，需要循环 index-1 次。O(n)
    :param head: 头结点
    :param index: 要访问的索引
    :return:
    """
    for _ in range(index):
        if head is None:
            return None
        head = head.next
    return head


def find(head: ListNode, target: int) -> int:
    """
    查找结点。O(n)
    :param head:
    :param target:
    :return:
    """
    index = 0
    while head:
        if head.value == target:
            return index
        index += 1
        head = head.next
    return -1


def main():
    # 初始化列表
    n0 = ListNode(1)
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(5)
    n4 = ListNode(4)

    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4

    # 插入，13254 -> 103254
    p = ListNode(0)
    insert(n0, p)

    # 删除 103254 -> 13254
    delete(n0)

    # 访问
    node: ListNode = access(n0, 2)
    assert node.value == 2, node

    # 查找
    index: int = find(n0, 0)
    assert index == -1, index

    index: int = find(n0, 2)
    assert index == 2, index


if __name__ == "__main__":
    main()
