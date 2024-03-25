"""
基于链表实现的队列，头结点和尾结点分别视为队首和队尾，队尾仅可添加元素，队首仅可删除元素
时间复杂度：
push O(n)
pop O(1)
peek O(1)
to_list O(n)
"""


class ListNode:
    def __init__(self, value: int):
        self.value: int = value
        self.next: ListNode | None = None


class Queue:
    def __init__(self):
        self._front: ListNode | None = None
        self._rear: ListNode | None = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, value: int):
        node = ListNode(value)
        if self.is_empty():
            self._rear = node
            self._front = node
        else:
            self._rear.next = node
            self._rear = node
        self._size += 1

    def pop(self) -> int:
        front_node = self._get_front_node()
        self._front = front_node.next
        self._size -= 1
        return front_node.value

    def peek(self) -> int:
        return self._get_front_node().value

    def _get_front_node(self) -> ListNode | None:
        if self.is_empty():
            raise IndexError("队列为空")
        node = self._front
        return node

    def to_list(self) -> list:
        node = self._front
        res = []
        while node:
            res.append(node.value)
            node = node.next
        return res

    def __str__(self) -> str:
        return str(self.to_list())


que = Queue()

# 入队
que.push(1)
que.push(3)
que.push(2)
que.push(5)
que.push(4)
print(f"[linkedList queue] {que}")

# 访问队首元素
front: int = que.peek()
print(f"[linkedList queue front] {front}")

# 出队
pop: int = que.pop()
print(f"[linkedList queue pop] {pop}")
print(f"[linkedList queue] {que}")

# 获取队列长
size: int = que.size()
print(f"[linkedList queue size] {size}")

# 判断队列是否为空
is_empty: bool = que.is_empty()
print(f"[linkedList queue is empty] {is_empty}")
