# coding=gbk
"""
有效括号字符串为空?("")、"(" + A + ")"?或?A + B，其中?A 和?B?都是有效的括号字符串，+?代表字符串的连接。例如，""，"()"，"(())()"?和?"(()(()))"?都是有效的括号字符串。

如果有效字符串?S?非空，且不存在将其拆分为?S = A+B?的方法，我们称其为原语（primitive），其中?A 和?B?都是非空有效括号字符串。

给出一个非空有效字符串?S，考虑将其进行原语化分解，使得：S = P_1 + P_2 + ... + P_k，其中?P_i?是有效括号字符串原语。

对?S?进行原语化分解，删除分解中每个原语字符串的最外层括号，返回 S?。

?

示例 1：

输入："(()())(())"
输出："()()()"
解释：
输入字符串为 "(()())(())"，原语化分解得到 "(()())" + "(())"，
删除每个部分中的最外层括号后得到 "()()" + "()" = "()()()"。
示例 2：

输入："(()())(())(()(()))"
输出："()()()()(())"
解释：
输入字符串为 "(()())(())(()(()))"，原语化分解得到 "(()())" + "(())" + "(()(()))"，
删除每隔部分中的最外层括号后得到 "()()" + "()" + "()(())" = "()()()()(())"。
示例 3：

输入："()()"
输出：""
解释：
输入字符串为 "()()"，原语化分解得到 "()" + "()"，
删除每个部分中的最外层括号后得到 "" + "" = ""。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-outermost-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
解法一 : 计数法（找规律）
基本思路：设置一个计数器 count，左括号 +1，右括号减 1，等于 0 则找到外括号的终点。并且 0 后面的一个括号肯定也是外括号，可以直接跳过。
"""
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        target = ''
        count, i = 1, 1
        while i < len(S):
            count += 1 if S[i] == '(' else -1
            if count == 0:
                i += 2
                count += 1
                continue
            target = S[i]
            i += 1
        return target


"""
解法二 ：双指针法
一个指针记录最外层左括号的位置，一个指针记录最外层右括号的位置，当匹配到的时候，再把字符串切片相加。
"""
class Solution2:
    def removeOuterParentheses(self, S: str) -> str:
        target = ''
        count, p, q = 0, 0, 0
        while q < len(S):
            count += 1 if S[q] == '(' else -1
            if count == 0:
                target = target + S[p+1:q]
                p = q
                continue
            q += 1
        return target


result = Solution2()
print(result.removeOuterParentheses("(()())(())"))