"""
双向队列，使用标准库
deque double-ended-queue
push_first push_last
pop_first pop_last
peek_first peek_last
以上时间复杂度都为 O(1)
"""
from collections import deque

deque: deque[int] = deque()

# 元素入队
deque.append(2)
deque.append(5)
deque.append(4)
deque.appendleft(3)
deque.appendleft(1)

# 访问元素
front: int = deque[0]
rear: int = deque[-1]

# 元素出队
pop_front: int = deque.popleft()  # 队首出队
pop_rear: int = deque.pop()  # 队尾出队

# 长度
size: int = len(deque)

# 判断是否为空
is_empty: bool = size == 0

