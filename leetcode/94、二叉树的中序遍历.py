"""
给定一个二叉树，返回它的中序?遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
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
    def inorderTraversal(self, root: TreeNode):
        res = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        helper(root)
        return res


# 非递归
class Solution:
    def inorderTraversal(self, root: TreeNode):
        res, st = [], []
        while root or st:
            while root:
                st.append(root)
                root = root.left
            root = st.pop()
            res.append(root.val)
            root = root.right
        return res
