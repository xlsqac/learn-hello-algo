"""
链式地址，优化哈希冲突，每个 bucket 都是一个链表
"""


class HashMapChaining:
    def __init__(self):
        self.size = 0  # 键值对数量
        self.capacity = 4  # 哈希容量
        self.load_thres = 2.0 / 3.0  # 负载因子阈值
        self.extend_ratio = 2  # 扩容倍数
        self.buckets = [[] for _ in range(self.capacity)]  # 同数组

    def hash_func(self, key):
        return key % self.capacity

    def load_factor(self):
        return self.size / self.capacity
    