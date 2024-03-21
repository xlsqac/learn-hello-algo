"""
stack 栈的常用操作，直接把列表当成栈来使用
"""
stack: list[int] = []

# 入栈
stack.append(1)
stack.append(3)
stack.append(2)
stack.append(5)
stack.append(4)

# 访问栈顶
peek: int = stack[-1]

# 出栈
pop: int = stack.pop()

# 获取栈的长度
size: int = len(stack)

# 是否为空
is_empty: bool = len(stack) == 0
