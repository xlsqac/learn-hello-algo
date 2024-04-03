"""
基于双向链表实现的双向队列
为啥要用双向列表，不用单向列表
push_first push_last
pop_first pop_last
peek_first peek_last
以上的时间复杂度都为 O(1)
to_array O(n)
"""


class ListNode:
    def __init__(self, value: int):
        self.value: int = value
        self.next: ListNode | None = None  # 后继节点
        self.prev: ListNode | None = None  # 前驱节点


class LinkedListDeque:
    def __init__(self):
        self._front: ListNode | None = None
        self._rear: ListNode | None = None
        self._size: int = 0

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self.size() == 0

    def _push(self, value: int, is_front: bool) -> None:
        """
        push 公共实现，主要为了省略队列为空的情况

        :param value:
        :param is_front: 是否从队尾 push
        :return:
        """
        node = ListNode(value)
        if self.is_empty():
            self._front = self._rear = node
        elif is_front:
            self._front.prev = node
            node.next = self._front
            self._front = node
        else:
            self._rear.next = node
            node.prev = self._rear
            self._rear = node
        self._size += 1

    def push_first(self, value: int):
        """
        push 到队首
        :param value:
        :return:
        """
        self._push(value, True)

    def push_last(self, value: int):
        """
        push 到队尾
        :param value:
        :return:
        """
        self._push(value, False)

    def _peek(self, is_front: bool) -> int:
        if self.is_empty():
            raise IndexError("队列为空")
        elif is_front:
            num = self._front.value
        else:
            num = self._rear.value
        return num

    def _pop(self, is_front: bool = False) -> int:
        num: int = self._peek(is_front=is_front)
        if is_front:
            self._front = self._front.next
            self._front.prev = None
        else:
            self._rear = self._rear.prev
            self._rear.next = None
        self._size -= 1
        return num

    def pop_first(self) -> int:
        """
        从队首出队
        :return:
        """
        return self._pop(True)

    def pop_last(self) -> int:
        """
        从队尾出队
        :return:
        """
        return self._pop(False)

    def peek_first(self) -> int:
        return self._peek(True)

    def peek_last(self) -> int:
        return self._peek(False)

    def to_array(self) -> list:
        res = []
        front = self._front
        while front is not None:
            res.append(front.value)
            front = front.next

        return res


if __name__ == "__main__":
    # 初始化双向队列
    deque = LinkedListDeque()
    deque.push_last(3)
    deque.push_last(2)
    deque.push_last(5)
    print("双向队列 deque =", deque.to_array())

    # 访问元素
    peek_first: int = deque.peek_first()
    print("队首元素 peek_first =", peek_first)
    peek_last: int = deque.peek_last()
    print("队尾元素 peek_last =", peek_last)

    # 元素入队
    deque.push_last(4)
    print("元素 4 队尾入队后 deque =", deque.to_array())
    deque.push_first(1)
    print("元素 1 队首入队后 deque =", deque.to_array())

    # 元素出队
    pop_last: int = deque.pop_last()
    print("队尾出队元素 =", pop_last, "，队尾出队后 deque =", deque.to_array())
    pop_first: int = deque.pop_first()
    print("队首出队元素 =", pop_first, "，队首出队后 deque =", deque.to_array())

    # 获取双向队列的长度
    size: int = deque.size()
    print("双向队列长度 size =", size)

    # 判断双向队列是否为空
    is_empty: bool = deque.is_empty()
    print("双向队列是否为空 =", is_empty)
