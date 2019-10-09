"""
题目描述
输入一个链表，反转链表后，输出新链表的表头。
"""
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        new_head = None

        while pHead:
            tmp = pHead.next
            pHead.next = new_head
            new_head = pHead
            pHead = tmp

        return new_head