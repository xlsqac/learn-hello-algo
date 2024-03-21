"""
基于数组实现的栈，将数组的尾部视为栈顶，入栈和出栈都操作尾部
"""


class ArrayStack:
    def __init__(self):
        self._stack: list[int] = []

    def size(self):
        return len(self._stack)

    def is_empty(self):
        return self._stack == []

    def push(self, value: int):
        self._stack.append(value)

    def pop(self) -> int:
        self.check_index()
        return self._stack.pop()

    def peek(self) -> int:
        self.check_index()
        return self._stack[-1]

    def to_list(self) -> list:
        return self._stack

    def check_index(self) -> None:
        if self.is_empty():
            raise IndexError("栈为空")


def main():
    array_stack = ArrayStack()
    assert array_stack.is_empty() is True

    # array_stack.peek()  # index error

    array_stack.push(1)
    assert 1 == array_stack.peek()
    assert 1 == array_stack.pop()
    array_stack.push(1)
    array_stack.push(3)
    array_stack.push(2)
    array_stack.push(5)
    array_stack.push(4)
    assert [1, 3, 2, 5, 4] == array_stack.to_list(), array_stack.to_list()


if __name__ == "__main__":
    main()
