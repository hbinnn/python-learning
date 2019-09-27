"""
算法

初始化栈 S。
一次处理表达式的每个括号。
如果遇到开括号，我们只需将其推到栈上即可。这意味着我们将稍后处理它，让我们简单地转到前面的 子表达式。
如果我们遇到一个闭括号，那么我们检查栈顶的元素。如果栈顶的元素是一个 相同类型的 左括号，那么我们将它从栈中弹出并继续处理。否则，这意味着表达式无效。
如果到最后我们剩下的栈中仍然有元素，那么这意味着表达式无效。

作者：LeetCode
链接：https://leetcode-cn.com/problems/valid-parentheses/solution/you-xiao-de-gua-hao-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


def isValid(s):
    # 初始化栈
    stack = []
    # 初始化匹配
    mapping = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    # 遍历字符串
    for char in s:
        # 如果当前字符在匹配字典中，判断它与栈顶字符是否匹配，不匹配则提前退出函数返回False
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        # 如果当前字符不再匹配字典中，则入栈
        else:
            stack.append(char)

    return not stack


"""
方法二
我们从表达式的左侧开始，每次只处理一个括号。
假设我们遇到一个开括号（即 (），表达式是否无效取决于在该表达式的其余部分的某处是否有相匹配的闭括号（即 )）。此时，我们只是增加计数器的值保持跟踪现在为止开括号的数目。left += 1
如果我们遇到一个闭括号，这可能意味着这样两种情况：
此闭括号没有与与之对应的开括号，在这种情况下，我们的表达式无效。当 left == 0，也就是没有未配对的左括号可用时就是这种情况。
我们有一些未配对的开括号可以与该闭括号配对。当 left > 0，也就是有未配对的左括号可用时就是这种情况。
如果我们在 left == 0 时遇到一个闭括号（例如 )），那么当前的表达式无效。否则，我们会减少 left 的值，也就是减少了可用的未配对的左括号的数量。
继续处理字符串，直到处理完所有括号。
如果最后我们仍然有未配对的左括号，这意味着表达式无效。

作者：LeetCode
链接：https://leetcode-cn.com/problems/valid-parentheses/solution/you-xiao-de-gua-hao-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


def isValid2(s):
    left1 = 0
    left2 = 0
    left3 = 0

    for item in s:
        if item == '(':
            left1 += 1
        if item == ')':
            left1 -= 1
        if item == '[':
            left2 += 1
        if item == ']':
            left2 -= 1
        if item == '{':
            left3 += 1
        if item == '}':
            left3 -= 1

    if left1 == 0 and left2 == 0 and left3 == 0:
        print(True)
    else:
        print(False)


print(isValid("()(()"))


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(",
                   "}": "{",
                   "]": "["}
        for char in s:
            if char in mapping:
                top_elem = stack.pop() if stack else '#'
                if mapping[char] != top_elem:
                    return False
            else:
                stack.append(char)

        return not stack
