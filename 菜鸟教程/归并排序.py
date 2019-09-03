"""
 归并排序（英语：Merge sort，或mergesort），是创建在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。

分治法:

    分割：递归地把当前序列平均分割成两半。
    集成：在保持元素顺序的同时将上一步得到的子序列集成到一起（归并）。
"""

nums = [1, 5, 8, 1, 2, 4, 5]

# 1.递归拆分
# 2.分组排序
# 3.重组排序


def merge(left, right):
    result = []
    i = j = 0
    while len(left) > i and len(right)>j:
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(l):
    if len(l) <= 1:
        return l
    moddle = int(len(l)/2)
    left = merge_sort(l[0: moddle])
    right = merge_sort(l[moddle: len(l)])
    print('left:', left, 'right:', right)
    return merge(left, right)


if __name__ == '__main__':
    a =  merge_sort(nums)
    print(a)
    # def test(n):
    #     print '第一个n: %s' % n
    #     if n > 4:
    #         return
    #     test(n + 1)
    #     print '第二个n: %s' % n
    # test(1)