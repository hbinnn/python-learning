"""
题目描述
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return []

        result = []
        head = listNode

        while head:
            result.insert(0, head.val)
            head = head.next
        return result


# 递归
class Solution:
    def __init__(self):
        self.result = []

    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return []

        head = listNode
        if head:
            if head.next:
                self.printListFromTailToHead(head.next)
            self.result.append(head.val)

        return self.result
