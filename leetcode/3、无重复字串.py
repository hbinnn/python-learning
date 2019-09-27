"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
思路：
这道题主要用到思路是：滑动窗口

什么是滑动窗口？

其实就是一个队列,比如例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，当再进入 a，队列变成了 abca，这时候不满足要求。所以，我们要移动这个队列！

如何移动？

我们只要把队列的左边的元素移出就行了，直到满足题目要求！

一直维持这样的队列，找出队列出现最长的长度时候，求出解！

"""


def lengthOfLongestSubstring(s: str) -> int:
    # 如果字符串s为空，返回0
    if not s:
        return 0
    # 保存窗口内字符串
    lookup = list()
    n = len(s)
    # 最大子串长度
    max_len = 0
    # 当前窗口长度
    cur_len = 0
    # 遍历字符串s
    for i in range(n):
        val = s[i]
        # 如果该值不在窗口中
        if val not in lookup:
            # 添加到窗口内
            lookup.append(val)
            # 当前长度+1
            cur_len += 1
        # 如果该值在窗口中已存在
        else:
            # 获取其在窗口中的位置
            index = lookup.index(val)
            # 移除该位置及之前的字符，相当于上图中的图3到图4
            lookup = lookup[index + 1:]
            lookup.append(val)
            # 当前长度更新为窗口长度
            cur_len = len(lookup)
        # 如果当前长度大于最大长度，更新最大长度值
        if cur_len > max_len:
            max_len = cur_len
    # 返回最大子串长度
    return max_len


print(lengthOfLongestSubstring("abcdaefg"))