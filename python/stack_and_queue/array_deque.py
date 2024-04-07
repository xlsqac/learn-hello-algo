"""
基于环形数组实现的双向队列
"""


class ArrayDeque:
    def __init__(self, capacity: int):
        self._nums: list[int] = [0] * capacity
        self._front: int = 0
        self._size: int = 0

    def capacity(self) -> int:
        return len(self._nums)

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self.size() == 0

    def _index(self, i: int) -> int:
        return (i + self.capacity()) % self.capacity()

    def _push(self, num: int, is_front: bool) -> None:
        if self.size() == self.capacity():
            raise IndexError("队列已满")
        if is_front:
            # 队列为空时，push_first 放到数组的末尾
            index = self._index(self._front - 1)
            self._front = index
        else:
            # 队列为空时，push_last 直接放到数组的开头
            index = self._index(self._front + self._size)
        self._nums[index] = num
        self._size += 1

    def push_first(self, num: int) -> None:
        self._push(num, True)

    def push_last(self, num: int) -> None:
        self._push(num, False)

    def pop_first(self) -> int:
        num: int = self.peek_first()
        self._front = self._index(self._front + 1)
        self._size -= 1
        return num

    def pop_last(self) -> int:
        num: int = self.peek_last()
        self._size -= 1
        return num

    def _peek(self, index: int) -> int:
        if self.is_empty():
            raise IndexError("队列为空")
        return self._nums[index]

    def peek_first(self) -> int:
        self._peek(self._front)
        if self.is_empty():
            raise IndexError("队列为空")
        return self._nums[self._front]

    def peek_last(self) -> int:
        return self._peek(self._index(self._front + self._size - 1))

    def to_array(self) -> list[int]:
        res = [0] * self.size()
        for i in range(self._size):
            index = (self._front + i) % self.capacity()
            res[i] = self._nums[index]
        return res


if __name__ == "__main__":
    # 初始化双向队列
    deque = ArrayDeque(10)
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
