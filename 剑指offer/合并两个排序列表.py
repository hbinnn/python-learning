"""
题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        p1 = pHead1
        p2 = pHead2
        head = ListNode(0)
        new_head = head

        while p1 and p2:
            if p1.val <= p2.val:
                new_head.next = p1
                p1 = p1.next
            else:
                new_head.next = p2
                p2 = p2.next
            new_head = new_head.next
        new_head.next = p1 if p1 else p2

        return head.next