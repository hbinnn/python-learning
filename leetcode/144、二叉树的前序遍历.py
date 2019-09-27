"""
给定一个二叉树，返回它的?前序?遍历。

?示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归
class Solution:
    def preorderTraversal(self, root: TreeNode):
        res = []
        def helper(root):
            if root is None:
                return
            res.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return res


# 非递归
class Solution:
    def preorderTraversal(self, root: TreeNode):
        res, stack = [], []
        if not root:
            return
        stack.append(root)
        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return res