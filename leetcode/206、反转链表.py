"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None

        while head:
            tmp = head.next
            head.next = new_head
            new_head = head
            head = tmp
        return new_head


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        node_next = head.next
        res = self.reverseList(node_next)
        node_next.next = head
        head.next = None
        return res
