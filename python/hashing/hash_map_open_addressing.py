"""
开放寻址, 线性探测，当哈希冲突时，从冲突的索引开始一步一步找可存放的桶，步长通常为一
"""


class Pair:
    """键值对"""
    def __init__(self, k: int, v: str):
        self.key = k
        self.val = v


class HashMapOpenAddressing:
    def __init__(self):
        self.size = 0  # 键值对数量
        self.capacity = 4  # 键值对容量
        self.load_thres = 2.0 / 3.0  # 负载因子阈值
        self.extend_radio = 2  # 扩容倍数
        self.buckets: list[Pair | None] = [None] * self.capacity
        self.TOMBSTONE = Pair(-1, "-1")  # 删除标记

    def hash_func(self, key) -> int:
        return key % self.capacity

    def load_factor(self):
        return self.size / self.capacity

    def get(self, key) -> str | None:
        index = self.hash_func(key)
        bucket: Pair | None = self.buckets[index]

        if bucket:
            if bucket.key == key:
                return bucket.val
            index += 1
            for i in range(self.capacity-1):
                index = index + i % self.capacity
                if self.buckets[index].key == key:
                    return self.buckets[index].val
                elif self.buckets[index] is None:
                    return None

        return None

    def put(self, key, value):
        if self.load_factor() > self.load_thres:
            self.extend()

        index: int = self.hash_func(key)
        bucket = self.buckets[index]
        if bucket is None or bucket is self.TOMBSTONE:
            self.buckets[index] = Pair(key, value)
            self.size += 1
        else:
            index += 1
            for i in range(self.capacity - 1):
                index = index + i % self.capacity
                if self.buckets[index] is None or self.buckets[index] is self.TOMBSTONE:
                    self.buckets[index] = Pair(key, value)
                    self.size += 1
                    return

    def remove(self, key):
        index = self.hash_func(key)
        bucket: Pair | None = self.buckets[index]
        if bucket:
            if bucket.key == key:
                self.buckets[index] = self.TOMBSTONE
                self.size -= 1
                return
            index += 1
            for i in range(self.capacity - 1):
                index = index + i % self.capacity
                if self.buckets[index].key == key:
                    self.buckets[index] = self.TOMBSTONE
                    self.size -= 1
                    return
        return None

    def extend(self) -> None:
        buckets = self.buckets
        self.capacity *= self.extend_radio
        self.size = 0
        self.buckets: list[Pair | None] = [None] * self.capacity
        for pair in buckets:
            if pair not in (None, self.TOMBSTONE,):
                self.put(pair.key, pair.val)

    def print(self) -> None:
        for pair in self.buckets:
            if pair is None:
                print("None")
            elif pair is self.TOMBSTONE:
                print("TOMBSTONE")
            else:
                print(f"{pair.key} -> {pair.val}")


if __name__ == "__main__":
     # 初始化哈希表
    hashmap = HashMapOpenAddressing()

    # 添加操作
    # 在哈希表中添加键值对 (key, val)
    hashmap.put(12836, "小哈")
    hashmap.put(15937, "小啰")
    hashmap.put(16750, "小算")
    hashmap.put(13276, "小法")
    hashmap.put(10583, "小鸭")
    print("\n添加完成后，哈希表为\nKey -> Value")
    hashmap.print()

    # 查询操作
    # 向哈希表中输入键 key ，得到值 val
    name = hashmap.get(13276)
    print("\n输入学号 13276 ，查询到姓名 " + name)

    # 删除操作
    # 在哈希表中删除键值对 (key, val)
    hashmap.remove(16750)
    print("\n删除 16750 后，哈希表为\nKey -> Value")
    hashmap.print()

