"""
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

 

示例 1：

输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：

输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]
"""

"""

"""
from collections import Counter


# 哈希表
def findSubstring(s, words):

    if not s or not words:
        return []
    # 单个单词的长度
    one_word = len(words[0])
    # 需要匹配的总长度
    all_len = len(words) * one_word
    # 字符串长度
    n = len(s)
    words = Counter(words)
    res = []
    # 字符串切片起始位置
    for i in range(0, n - all_len + 1):
        # 每次取出单词总长度大小的字符串
        tmp = s[i:i + all_len]
        c_tmp = []
        # 对取出的字符串进行切片统计
        for j in range(0, all_len, one_word):
            c_tmp.append(tmp[j:j + one_word])
        # 如果跟需要匹配的单词相对应则匹配成功
        if Counter(c_tmp) == words:
            res.append(i)
    return res


# 滑动窗口
def findSubstring2(s, words):
    # 如果s或者word为空，返回0
    if not s or not words:
        return []
    # 单词的长度
    one_word = len(words[0])
    # 单词的个数
    word_num = len(words)
    # 字符串的长度
    n = len(s)
    # 如果字符串长度小于单词长度，返回0
    if n < one_word:
        return []
    # Counter返回一个以元素为key，元素个数为value的集合
    words = Counter(words)
    # res保存结果
    res = []
    # 选择字符串开始切片的位置，0--单词长度-1
    for i in range(0, one_word):
        # 用来标记是否所有单词都匹配
        cur_cnt = 0
        # 滑动窗口的左端点，也是匹配成功时的返回值
        left = i
        # 滑动窗口的右端点
        right = i
        # 定义一个对象
        cur_Counter = Counter()
        # 遍历字符串
        while right + one_word <= n:
            # 取出与单词长度相同的切片
            w = s[right:right + one_word]
            # 滑动窗口向右滑动
            right += one_word
            # 如果切片不在匹配的单词中
            if w not in words:
                # 滑动窗口的左端点右移
                left = right
                # 清除对象
                cur_Counter.clear()
                # 计数标志置零
                cur_cnt = 0
            else:
                # 匹配成功的对象个数加一
                cur_Counter[w] += 1
                # 技术标志加一
                cur_cnt += 1
                # 如果有多次匹配同一个单词，则将该单词从滑动窗口中取出
                while cur_Counter[w] > words[w]:
                    # 取滑动窗口最左边的单词
                    left_w = s[left:left + one_word]
                    # 窗口左端点右移
                    left += one_word
                    # 将多次匹配的对象个数减一
                    cur_Counter[left_w] -= 1
                    # 计数标志减一
                    cur_cnt -= 1
                # 如果计数标志等于单词数量则匹配成功
                if cur_cnt == word_num:
                    # 将左端点加入
                    res.append(left)
    return res


s = "barfoothefoobarman"
words = ["foo","bar"]
print(findSubstring2(s, words))