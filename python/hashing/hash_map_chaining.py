"""
链式地址，优化哈希冲突，每个 bucket 都是一个链表，使用列表替代链表，简化代码
哈希冲突时把数据放在同一个列表中，取的时候先取到整个桶，然后遍历这个桶找相同的 key
"""


class Pair:
    """键值对"""
    def __init__(self, k: int, v: str):
        self.key = k
        self.val = v


class HashMapChaining:
    def __init__(self):
        self.size = 0  # 键值对数量
        self.capacity = 4  # 哈希容量
        self.load_thres = 2.0 / 3.0  # 负载因子阈值
        self.extend_ratio = 2  # 扩容倍数
        self.buckets = [[] for _ in range(self.capacity)]  # 同数组

    def hash_func(self, key) -> int:
        return key % self.capacity

    def load_factor(self) -> float:
        return self.size / self.capacity

    def get(self, key) -> str | None:
        index = self.hash_func(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair.key == key:
                return pair.val
        return None

    def put(self, key, value) -> None:
        if self.load_factor() > self.load_thres:
            self.extend()
        index = self.hash_func(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair.key == key:
                pair.val = value
                return
        bucket.append(Pair(key, value))
        self.size += 1

    def remove(self, key) -> None:
        index = self.hash_func(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair.key == key:
                bucket.remove(pair)
                self.size -= 1
                return

    def extend(self) -> None:
        """扩容哈希表"""
        # 暂存哈希表
        buckets = self.buckets
        self.capacity *= self.extend_ratio
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        for bucket in buckets:
            for pair in bucket:
                self.put(pair.key, pair.val)

    def print(self) -> None:
        for bucket in self.buckets:
            res = []
            for pair in bucket:
                res.append(f"{pair.key} -> {pair.val}")
            print(res)


if __name__ == "__main__":
    # 初始化哈希表
    hashmap = HashMapChaining()

    # 添加操作
    # 在哈希表中添加键值对 (key, value)
    hashmap.put(12836, "小哈")
    hashmap.put(15937, "小啰")
    hashmap.put(16750, "小算")
    hashmap.put(13276, "小法")
    hashmap.put(10583, "小鸭")
    print("\n添加完成后，哈希表为\n[Key1 -> Value1, Key2 -> Value2, ...]")
    hashmap.print()

    # 查询操作
    # 向哈希表中输入键 key ，得到值 value
    name = hashmap.get(13276)
    print("\n输入学号 13276 ，查询到姓名 " + name)

    # 删除操作
    # 在哈希表中删除键值对 (key, value)
    hashmap.remove(12836)
    print("\n删除 12836 后，哈希表为\n[Key1 -> Value1, Key2 -> Value2, ...]")
    hashmap.print()

