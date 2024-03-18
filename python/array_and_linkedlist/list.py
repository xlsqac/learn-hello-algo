"""
列表及其相关操作，可以将列表看为动态数组
1. 随机访问 O(1)
2. 更新指定索引元素 O(1)
3. 插入元素 O(n)
4. 追加元素 O(1)
5. 删除元素 O(n)
6. 遍历 O(n)
7. 合并列表 O(m+n)
8. 排序 O(n)
"""


def access(nums: list[int], index: int) -> int:
    """
    访问元素，O(1)
    :param nums: 数据源
    :param index: 索引
    :return: int
    """
    return nums[index]


def update(nums: list[int], index: int, val: int) -> None:
    """
    更新元素，O(1)
    :param nums: 数据源
    :param index: 索引
    :param val: 更新的值
    :return:
    """
    nums[index] = val


def insert(nums: list[int], index: int, val: int) -> None:
    """
     插入元素，O(n)
    :param nums:
    :param index:
    :param val:
    :return:
    """
    nums.insert(index, val)


def append(nums: list[int], val: int) -> None:
    """
    追加元素，O(1)
    :param nums:
    :param val:
    :return:
    """
    nums.append(val)


def pop(nums: list[int], index: int) -> None:
    """
    删除元素，O(n)
    :param nums:
    :param index:
    :return:
    """
    nums.pop(index)


def reverse(nums: list[int]) -> None:
    """
    遍历列表，O(n)
    :param nums:
    :return:
    """
    for num in nums:
        print(num)


def extend(nums: list[int], nums1: list[int]) -> list[int]:
    """
    拼接列表, O(m+n)
    :param nums:
    :param nums1:
    :return:
    """
    return nums + nums1


def sort(nums: list[int]) -> None:
    """
    排序， O(n)
    :param nums:
    :return:
    """
    nums.sort()


def main():
    nums1: list[int] = []
    nums: list[int] = [1, 3, 2, 5, 4]

    # 访问元素
    assert access(nums, 0) == 1
    # 更新元素
    update(nums, 0, 10)
    assert nums[0] == 10

    # 插入
    insert(nums, 1, 200)
    assert nums == [10, 200, 3, 2, 5, 4]

    # 追加
    append(nums, 300)
    assert nums == [10, 200, 3, 2, 5, 4, 300]

    # 删除
    pop(nums, 3)
    assert nums == [10, 200, 3, 5, 4, 300]

    # 遍历
    print("[reverse nums]")
    reverse(nums)

    # 合并两个列表
    append(nums1, 1000)
    nums2 = extend(nums, nums1)
    assert nums2 == [10, 200, 3, 5, 4, 300, 1000]

    # 排序
    sort(nums)
    assert nums == [3, 4, 5, 10, 200, 300]


if __name__ == "__main__":
    main()
