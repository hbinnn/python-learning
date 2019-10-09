"""
题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""
# 方法一：replace
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        return s.replace(' ', '%20')


# 方法二：列表
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        s = list(s)
        for i in range(len(s)):
            if s[i] == ' ':
                s[i] = '%20'

        return ''.join(s)