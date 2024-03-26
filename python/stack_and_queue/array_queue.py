"""
基于数组实现的队列，头结点和尾结点分别视为队首和队尾，队尾仅可添加元素，队首仅可删除元素
时间复杂度：
push O(1)
pop O(1)，出队效率比较低，采用其他方式，增加出队效率
peek O(1)
to_list O(n)

提升出队效率：
出队不会真的删除队首元素，而是用一个变量来确定当前队首在数组中的索引，这样可以让 pop 达到 O(1)
指针移动：
不断出队入队时 front 会一直往右移动，当移动到最右边时需要重回最左边
采用进制的思想，逢 cap 进 1，front = (front + 1) % cap，利用取余操作算出索引
push pop to_list 都需要这样计算索引
"""


class ArrayQueue:
    def __init__(self, size: int):
        self._arr: list[int] = [0] * size
        self._size: int = 0
        self._front: int = 0  # 维护队首的索引，用于提升 pop 的效率

    def capacity(self) -> int:
        return len(self._arr)

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def push(self, value: int) -> None:
        if self._size == self.capacity():
            raise IndexError("队列已满")
        # 先计算 push 进来的元素保存在数组中的索引
        # 在这里将数组视为环形数组，当队列不满的时候，push 进来的元素可能需要加到数组前端
        # eg: 2 3 4 5 6 7 8 9 0 1，size = 9 front = 9，该队列为 1 2 3 4 5 6 7 8 9
        # 此时 push(10)，10 应该放在数组[8]处
        # 利用进制的思想，逢 cap 进 1，在这里也就是逢 10 就从数组开头计算，如果算出 10 那就应该存在索引 0 处
        # 所以利用取余操作  (self._size + self._front) % self.capacity()
        rear = (self._front + self._size) % self.capacity()
        self._arr[rear] = value
        self._size += 1

    def pop(self) -> int:
        num: int = self.peek()
        self._front += (self._front + 1) % self.capacity()
        self._size -= 1
        return num

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("队列为空")
        return self._arr[self._front]

    def to_list(self) -> list[int]:
        # 2 3 4 5 6 7 8 9 0 1
        # front 9 size 9
        # return 1 2 3 4 5 6 7 8 9
        # list[i] 9 0 1 2 3 4 5 6 7
        # range times size
        # range start front 9 10 11 12 13 14 15 16 17
        # i 0 - 8

        res = [0] * self._size
        for i in range(self._size):
            res[i] = self._arr[(self._front + i) % self.capacity()]
        return res

    def __str__(self) -> str:
        return str(self.to_list())


que = ArrayQueue(10)

# 入队
que.push(1)
que.push(2)
que.push(3)
que.push(4)
que.push(5)
print(f"[array queue] {que}")

# 访问队首元素
front: int = que.peek()
print(f"[array queue front] {front}")

# 出队
pop: int = que.pop()
print(f"[array queue pop] {pop}")

# 获取队列长度
size: int = que.size()
print(f"[array queue size] {size}")

# 判断队列是否为空
is_empty: bool = que.is_empty()
print(f"[array queue is empty] {is_empty}")
