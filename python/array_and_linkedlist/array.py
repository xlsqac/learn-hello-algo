"""
数组创建以及操作
1. 随机访问，时间复杂度 O(1)
"""
import random


def random_access(arr: list[int]):
    """
    随机访问，随机生成一个索引，获取该索引对应的值，索引范围为 0 ~ len(arr) -1
    时间复杂度：O(1)
    :param arr: 访问的数组
    :return: int 访问的元素
    """
    index = random.randint(0, len(arr) - 1)
    return arr[index]


def insert(arr: list[int], index: int, value: int):
    """
    插入元素，插入后要将后面的元素后移一位
    时间复杂度：O(n)
    :param arr: 数据源
    :param index: 插入的索引
    :param value: 插入的值
    :return:
    """
    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i - 1]
    arr[index] = value


def remove(arr: list[int], index: int):
    """
    删除索引 index 处的元素
    时间复杂度：O(n)
    :param arr: 数据源
    :param index: 要删除的索引
    :return:
    """
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1]


def traverse(arr: list[int]):
    """
    遍历数组
    时间复杂度：O(n)
    :param arr: 数据源
    :return:
    """
    for value in arr:
        print(value)


def find(arr: list[int], target: int):
    """
    查找元素，查到返回元素索引，没有返回 -1，数组是线性数据，所以也称线性查找
    时间复杂度：O(n)
    :param arr: 数据源
    :param target: 目标元素
    :return: index or -1
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


if __name__ == "__main__":

    # 创建一个数组
    arr: list[int] = [1, 3, 2, 5, 4]

    # 随机访问
    num = random_access(arr)
    print(f"[random_access] {num}")

    # 插入元素
    insert(arr, 2, 10)
    print(arr)

    # 删除元素
    remove(arr, 2)
    print(arr)

    # 遍历数组
    traverse(arr)

    # 查找元素
    assert find(arr, 2) == 2
    assert find(arr, 100) == -1

