"""
哈希表的常用操作
增加元素，删除元素，访问元素 O(1)
"""


hmap: dict = {}

hmap[12836] = "小哈"
hmap[15937] = "小啰"
hmap[16750] = "小算"
hmap[13276] = "小法"
hmap[10583] = "小鸭"

name: str = hmap[15937]

hmap.pop(10583)

# 遍历
# 遍历键值对
# 遍历键
# 遍历值

for key, value in hmap.items():
    print(f"{key}: {value}")


for key in hmap:
    print(key)

for value in hmap.values():
    print(value)
