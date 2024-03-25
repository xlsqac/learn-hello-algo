"""
队列的操作，使用自带队列类
push, pop, peek
"""
from collections import deque  # 双向队列

que: deque[int] = deque()

# 入队
que.append(1)
que.append(3)
que.append(2)
que.append(5)
que.append(4)
print(f"[queue] {que}")

# 访问队首元素
front: int = que[0]
print(f"[queue front] {front}")

# 出队
pop: int = que.popleft()
print(f"[queue pop] {pop}")

# 获取队列长度
size: int = len(que)
print(f"[queue size] {size}")

# 判断队列是否为空
is_empty: bool = size == 0
print(f"[queue is empty] {is_empty}")
