class MyList:
    def __init__(self):
        self._capacity: int = 10  # 容量
        self._arr: list[int] = [0] * self._capacity  # 数组
        self._size: int = 0
        self._extend_ratio = 2  # 每次列表扩容的倍数

    def size(self) -> int:
        return self._size

    def capacity(self) -> int:
        return self._capacity

    def get(self, index: int) -> int:
        self.check_index(index)
        return self._arr[index]

    def set(self, index: int, value: int) -> None:
        self.check_index(index)
        self._arr[index] = value

    def add(self, value: int) -> None:
        if self.size() == self.capacity():
            self.extend_ratio()
        self._arr[self._size] = value
        self._size += 1

    def insert(self, index: int, value: int) -> None:
        # 容量满了需要先扩容
        self.check_index(index)
        if self.size() == self.capacity():
            self.extend_ratio()
        for i in range(self.size() - 1, index - 1, -1):
            self._arr[i+1] = self._arr[i]
        self._arr[index] = value
        self._size += 1

    def remove(self, index: int) -> None:
        self.check_index(index)
        for i in range(index, self.size() - 1):
            self._arr[i] = self._arr[i+1]
        self._size -= 1

    def extend_ratio(self):
        self._arr = self._arr + [0] * self.capacity() * (self._extend_ratio - 1)
        self._capacity = len(self._arr)

    def to_array(self) -> list:
        return self._arr[:self._size]

    def check_index(self, index: int) -> None:
        if index < 0 or index >= self.size():
            raise IndexError("索引越界")


def main():
    # 初始化列表
    nums = MyList()
    # 在尾部添加元素
    nums.add(1)
    nums.add(3)
    nums.add(2)
    nums.add(5)
    nums.add(4)
    print(f"列表 nums = {nums.to_array()} ，容量 = {nums.capacity()} ，长度 = {nums.size()}")

    # 在中间插入元素
    nums.insert(3, 6)
    print("在索引 3 处插入数字 6 ，得到 nums =", nums.to_array())

    # 删除元素
    nums.remove(3)
    print("删除索引 3 处的元素，得到 nums =", nums.to_array())

    # 访问元素
    num = nums.get(1)
    print("访问索引 1 处的元素，得到 num =", num)

    # 更新元素
    nums.set(1, 0)
    print("将索引 1 处的元素更新为 0 ，得到 nums =", nums.to_array())

    # 测试扩容机制
    for i in range(10):
        # 在 i = 5 时，列表长度将超出列表容量，此时触发扩容机制
        nums.add(i)
    print(f"扩容后的列表 {nums.to_array()} ，容量 = {nums.capacity()} ，长度 = {nums.size()}")


if __name__ == "__main__":
    main()
