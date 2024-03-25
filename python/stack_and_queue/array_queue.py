"""
基于数组实现的队列，头结点和尾结点分别视为队首和队尾，队尾仅可添加元素，队首仅可删除元素
时间复杂度：
push O(1)
pop O(n)，出队效率比较低，采用其他方式，增加出队效率
peek O(1)
to_list O(1)

提升出队效率：
出队不会真的删除队首元素，而是用一个变量来确定当前队首在数组中的索引，这样可以让 pop 达到 O(1)
"""


class ArrayQueue:
    def __init__(self, size: int):
        self._arr: list[int] = [0] * size
        self._size: int = 0
        self._front: int = 0  # 维护队首的索引，用于提升 pop 的效率
        self._rear: int = 0

    def capacity(self) -> int:
        return len(self._arr)

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def push(self, value: int) -> None:
        if self._size == self.capacity():
            raise IndexError("队列已满")
        rear: int = (self._front + self._size) % self.capacity()
        self._arr[rear] = value
        self._rear += 1
        self._size += 1

    def pop(self) -> int:
        num: int = self.peek()
        self._front = (self._front + 1) % self.capacity()
        self._size -= 1
        return num

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("队列为空")
        return self._arr[self._front]

    def to_list(self) -> list[int]:
        print(self._arr)
        res = [0] * self.size()
        j: int = self._front
        for i in range(self.size()):
            res[i] = self._arr[j % self.capacity()]
            j += 1
        return res

    def __str__(self) -> str:
        return str(self.to_list())


que = ArrayQueue(10)

# 入队
que.push(1)
que.push(3)
que.push(2)
que.push(5)
que.push(4)
print(f"[array queue] {que}")

# 访问队首元素
front: int = que.peek()
print(f"[array queue front] {front}")

# 出队
pop: int = que.pop()
print(f"[array queue pop] {pop}")
print(f"[array queue] {que}")
que.push(4)
que.push(4)
que.push(4)
que.push(4)
que.push(4)
que.push(10)
print(f"[array queue] {que}")

# 获取队列长度
size: int = que.size()
print(f"[array queue size] {size}")

# 判断队列是否为空
is_empty: bool = que.is_empty()
print(f"[array queue is empty] {is_empty}")
