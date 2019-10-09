"""
题目描述
输入一个链表，输出该链表中倒数第k个结点。
"""
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if not head:
            return
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for _ in range(k):
            second = second.next
            if second is None:
                return
        while second:
            first = first.next
            second = second.next
        return first