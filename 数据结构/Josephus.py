#coding=gbk
import List
"""
n个人围坐一圈，从第k个人开始报数，报到第m个数的人退出。要求按顺序输出各出列人的序号
"""


# 基于python的list和固定大小的数组
def josephus_A(n, k, m):
    people = list(range(1, n+1))

    # 第k个人的下标
    i = k-1
    for num in range(n):
        count = 0
        while count < m:
            # 跳过已出列的人
            if people[i] > 0:
                count += 1
            # 将元素置零表示已出列
            if count == m:
                print(people[i], end='')
                people[i] = 0
            # 当数到数组最后一个人时，返回第一个人
            i = (i+1) % n
        if num < n-1:
            print(', ', end='')
        else:
            print('')
    return


# 基于顺序表的解
def josephus_L(n, k, m):
    people = list(range(1, n+1))
    # num表示表的长度，i表示下标
    num, i = n, k-1
    # 每删除一个元素，表的长度减1
    for num in range(n, 0, -1):
        i = (i+m-1) % num
        print(people.pop(i), end=', ' if num>1 else '\n')
    return


# 基于循环单链表的解
class Josephus(List.LCList):
    # 循环表对象的rear指针沿next方向移动m步
    def turn(self, m):
        for i in range(m):
            self._rear = self._rear.next

    def __init__(self, n, k, m):
        List.LCList.__init__(self)
        for i in range(n):
            self.append(i+1)
        self.turn(k-1)
        while not self.is_empty():
            self.turn(m-1)
            print(self.pop(), end=('\n' if self.is_empty() else ', '))


josephus_A(10, 2, 7)
josephus_L(10, 2, 7)
Josephus(10, 2, 7)