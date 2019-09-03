"""
堆排序是利用 堆进行排序的
堆是一种完全二叉树
堆有两种类型: 大根堆 小根堆

两种类型的概念如下：
大根堆：每个结点的值都大于或等于左右孩子结点
小根堆：每个结点的值都小于或等于左右孩子结点
参考链接：https://www.jianshu.com/p/d174f1862601

下面我们来看下堆排序的思想是怎样的(以大根堆为例)：
    首先将待排序的数组构造出一个大根堆
    取出这个大根堆的堆顶节点(最大值)，与堆的最下最右的元素进行交换，然后把剩下的元素再构造出一个大根堆
    重复第二步，直到这个大根堆的长度为1，此时完成排序。

"""

from collections import deque


def swap_param(L, i, j):
    L[i], L[j] = L[j], L[i]
    return L


def heap_adjust(L, start, end):
    temp = L[start]

    i = start
    j = 2 * i

    while j <= end:
        if (j < end) and (L[j] < L[j + 1]):
            j += 1
        if temp < L[j]:
            L[i] = L[j]
            i = j
            j = 2 * i
        else:
            break
    L[i] = temp


def heap_sort(L):
    L_length = len(L) - 1

    first_sort_count = int(L_length / 2)
    for i in range(first_sort_count):
        heap_adjust(L, first_sort_count - i, L_length)

    for i in range(L_length - 1):
        L = swap_param(L, 1, L_length - i)
        heap_adjust(L, 1, L_length - i - 1)

    return [L[i] for i in range(1, len(L))]


def main():
    L = deque([50, 16, 30, 10, 60,  90,  2, 70, 80])
    L.appendleft(0)
    print(heap_sort(L))


if __name__ == '__main__':
    main()