"""
基于链表实现的栈，入栈就是增加头结点，出栈就是删除头结点
"""


class ListNode:
    def __init__(self, value: int):
        self.value: int = value
        self.next: ListNode | None = None


class LinkedListStack:
    def __init__(self):
        self._peek: ListNode | None = None
        self._size: int = 0

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def push(self, value: int) -> None:
        """
        入栈，O(1)
        :param value:
        :return:
        """
        node = ListNode(value)
        node.next = self._peek
        self._peek = node
        self._size += 1

    def pop(self) -> int:
        """
        出栈，O(1)
        :return:
        """
        val = self.peek()
        self._peek = self._peek.next
        self._size -= 1
        return val

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("栈为空")
        val = self._peek.value
        return val

    def to_list(self) -> list:
        """
        转成 list，O(n)
        :return:
        """
        res = []
        head = self._peek
        while head:
            res.append(head.value)
            head = head.next
        res.reverse()
        return res


def main():
    lls = LinkedListStack()
    assert lls.is_empty() is True

    # lls.peek()  index error

    lls.push(1)
    assert 1 == lls.peek()
    assert 1 == lls.pop()
    lls.push(1)
    lls.push(3)
    lls.push(2)
    lls.push(5)
    lls.push(4)
    assert [1, 3, 2, 5, 4] == lls.to_list(), lls.to_list()


if __name__ == "__main__":
    main()
