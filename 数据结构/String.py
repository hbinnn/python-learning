# coding=gbk
# 朴素的串匹配算法
def naive_matching(target, pattern):
    m, n = len(target), len(pattern)
    i, j = 0, 0
    # i==m说明找到匹配
    while i<m and j<n:
        # 字符相同考虑下一对字符
        if target[j] == pattern[i]:
            i, j = i+1, j+1
        # 字符不同考虑target中下一位置
        else:
            i, j = 0, j-i+1
    # 找到匹配返回其开始下标
    if i == m:
        return j-1
    # 无匹配返回特殊值
    return -1


def matching_KMP(t, p, pnext):
    j, i = 0, 0
    n, m = len(t), len(p)
    while j<n and i<m:
        if i == -1 or t[j] == p[i]:
            i, j = i+1, j+1
        else:
            i = pnext[i]
        if i == m:
            return j-1
    return -1


def gen_pnext(p):
    """生成针对p中各个位置i的下一检查位置表，用于KMP算法"""
    i, k, m = 0, -1, len(p)
    # 初始元素全为-1
    pnext = [-1] * m
    while i < m-1:
        if k == -1 or p[i] == p[k]:
            i, k = i+1, k+1
            if p[i] == p[k]:
                pnext[i] = pnext[k]
            else:
                pnext[i] = k
        else:
            k = pnext[k]
    return pnext


def match(re, text):
    def match_here(re, i, text, j):
        """检查从text[j]开始的正文是否与re[i]开始的模式匹配"""
        while True:
            if i == rlen:
                return True
            if re[i] == '$':
                return i+1 == rlen and j == tlen
            if i+1 < rlen and re[i+1] == '*':
                return match_star(re[i], re, i+2, text, j)
            if j == tlen or (re[i] != '.' and re[i] != text[j]):
                return False
            i, j = i+1, j+1

    def match_star(c, re, i, text, j):
        """在text里跳过0个或多个c后检查匹配"""
        for n in range(j, tlen):
            if match_here(re, i, text, n):
                return True
            if text[n] != c and c != '.':
                break
        return False

    rlen, tlen = len(re), len(text)
    if re[0] == '^':
        if match_here(re, 1, text, 0):
            return 1
    for n in range(tlen):
        if match_here(re, 0, text, n):
            return n
    return -1

pnext = gen_pnext('abbcabcaabbcaa')
print(matching_KMP('ababcabcacbab', 'bcabc', pnext))