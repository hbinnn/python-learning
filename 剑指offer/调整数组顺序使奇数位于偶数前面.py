"""
题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""
class Solution:
    def reOrderArray(self, array):
        res1 = []
        res2 = []
        for i in array:
            if i % 2 == 0:
                res1.append(i)
            else:
                res2.append(i)
        return res2+res1


#  * 1.要想保证原有次序，则只能顺次移动或相邻交换。
#  * 2.i从左向右遍历，找到第一个偶数。
#  * 3.j从i+1开始向后找，直到找到第一个奇数。
#  * 4.将[i,...,j-1]的元素整体后移一位，最后将找到的奇数放入i位置，然后i++。
#  * 5.終止條件：j向後遍歷查找失敗。
class Solution:
    def reOrderArray(self, array):
        if not array:
            return []
        i = 0
        while i < len(array):
            while i < len(array) and array[i] % 2 == 1:
                i += 1
            j = i + 1
            while j < len(array) and array[j] % 2 == 0:
                j += 1
            if j < len(array):
                tmp = array[j]
                for k in range(j, i, -1):
                    array[k] = array[k - 1]
                array[i] = tmp
            else:
                break
        return array
