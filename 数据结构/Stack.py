import List


class StackUnderflow(ValueError):
    pass


# 基于顺序表的栈
class SStack():
    # 所有的栈操作都映射到list中
    def __init__(self):
        self._elem = []

    def is_empty(self):
        return self._elem == []

    def top(self):
        if self._elem == []:
            raise StackUnderflow("in SStack.top()")
        return self._elem[-1]

    def push(self, elem):
        self._elem.append(elem)

    def pop(self):
        if self._elem == []:
            raise StackUnderflow("in SStack.pop()")
        return self._elem.pop()


# 基于链接表的栈
class LStack():
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise StackUnderflow("in LStack.top()")
        return self._top.elem

    def push(self, elem):
        self._top = List.LNode(elem, self._top)

    def pop(self):
        if self._top is None:
            raise StackUnderflow("in LStack.pop()")
        p = self._top
        self._top = p.next
        return p.elem


"""
栈用于颠倒一组元素的顺序
ss1 = SStack()
for x in list1:
    ss1.push(x)
list2 = []
while not ss1.is_empty():
    list2.append(ss1.pop())
"""


def check_parens(text):
    """括号配对检查函数，text是被检查的正文"""
    # 括号匹配问题
    parens = "{}[]()"  # 所有括号
    open_parens = "{[("  # 开括号字符
    # 表示配对关系的字典
    opposite = {")": "(",
                "]": "[",
                "}": "{"
                }

    def parentheses(text):
        """括号生成器，每次调用返回text里的下一括号及其位置"""
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in parens:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1

    # 保存括号的栈
    st = SStack()
    # 对text里各括号和位置迭代
    for pr, i in parentheses(text):
        # 开括号，压进栈并继续
        if pr in open_parens:
            st.push(pr)
        # 栈顶不匹配就是失败
        elif st.pop() != opposite[pr]:
            print("Unmatching is found at", i, "for", pr)
            return False
        else:
            pass

    print("All parentheses are correctly matched.")
    return True