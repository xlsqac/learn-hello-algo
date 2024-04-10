"""
基于数组实现的哈希表
get, put, remove O(1)
"""


class Pair:
    """键值对"""
    def __init__(self, k: int, v: str):
        self.key = k
        self.val = v


class ArrayHashMap:
    def __init__(self):
        self.buckets: list[Pair | None] = [None] * 100

    def get(self, key: int) -> str:
        index = hash(key) % 100
        pair = self.buckets[index]
        return pair.val

    def put(self, key: int, value: str) -> None:
        index = hash(key) % 100
        pair = Pair(key, value)
        self.buckets[index] = pair

    def remove(self, key: int) -> None:
        index = hash(key) % 100
        self.buckets[index] = None

    def entry_set(self) -> list[Pair]:
        output = []
        for bucket in self.buckets:
            if bucket is not None:
                output.append(bucket)
        return output

    def key_set(self) -> list[int]:
        output = []
        for bucket in self.buckets:
            if bucket is not None:
                output.append(bucket.key)
        return output

    def value_set(self) -> list[str]:
        output = []
        for bucket in self.buckets:
            if bucket is not None:
                output.append(bucket.val)
        return output

    def print(self) -> None:
        for bucket in self.buckets:
            if bucket is not None:
                print(f"{bucket.key}: {bucket.val}")

if __name__ == "__main__":
    # 初始化哈希表
    hmap = ArrayHashMap()

    # 添加操作
    # 在哈希表中添加键值对 (key, value)
    hmap.put(12836, "小哈")
    hmap.put(15937, "小啰")
    hmap.put(16750, "小算")
    hmap.put(13276, "小法")
    hmap.put(10583, "小鸭")
    print("\n添加完成后，哈希表为\nKey -> Value")
    hmap.print()

    # 查询操作
    # 向哈希表中输入键 key ，得到值 value
    name = hmap.get(15937)
    print("\n输入学号 15937 ，查询到姓名 " + name)

    # 删除操作
    # 在哈希表中删除键值对 (key, value)
    hmap.remove(10583)
    print("\n删除 10583 后，哈希表为\nKey -> Value")
    hmap.print()

    # 遍历哈希表
    print("\n遍历键值对 Key->Value")
    for pair in hmap.entry_set():
        print(pair.key, "->", pair.val)

    print("\n单独遍历键 Key")
    for key in hmap.key_set():
        print(key)

    print("\n单独遍历值 Value")
    for val in hmap.value_set():
        print(val)

