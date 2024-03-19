class MyList:
    def __init__(self):
        self._capacity: int = 10  # 容量
        self._arr: list[int] = [0] * self._capacity  # 数组
        self._size: int = 0
        self._extend_ratio = 2  # 每次列表扩容的倍数

    def check_index(func):
        def wrapper(self, *args, **kwargs):
            index = args[1]
            if index < 0 or index >= self.size():
                raise IndexError("索引越界")
            return func
        return wrapper

    def size(self) -> int:
        return self._size

    def capacity(self) -> int:
        return self._capacity

    @check_index
    def get(self, index: int) -> int:
        return self._arr[index]

    @check_index
    def set(self, index: int, value: int) -> None:
        self._arr[index] = value

    def add(self, value: int) -> None:
        if self.size() == self.capacity():
            self.extend_ratio()
        self._arr[self._size] = value
        self._size += 1

    @check_index
    def insert(self, index: int, value: int) -> None:
        # 容量满了需要先扩容
        if self.size() == self.capacity():
            self.extend_ratio()
        for i in range(self.size() - 1, index - 1, -1):
            self._arr[i] = self._arr[i-1]
        self._arr[index] = value
        self._size += 1

    @check_index
    def remove(self, index: int) -> None:
        for i in range(index, self.size() - 1):
            self._arr[i] = self._arr[i+1]
        self._size -= 1

    def extend_ratio(self):
        self._arr = self._arr + [0] * self.capacity() * (self._extend_ratio - 1)
        self._capacity = len(self._arr)

    def to_array(self) -> list:
        return self._arr[:self._size]


def main():
    my_list = MyList()
    my_list.add(1)
    print(my_list.to_array())
    my_list.insert(-1, 1)


if __name__ == "__main__":
    main()
