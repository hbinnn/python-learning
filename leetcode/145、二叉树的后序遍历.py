# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# µÝ¹é
class Solution:
    def postorderTraversal(self, root: TreeNode):
        res = []

        def helper(node):
            if not node:
                return
            helper(node.left)
            helper(node.right)
            res.append(node.val)
        helper(root)
        return res


# µü´ú
class Solution:
    def postorderTraversal(self, root: TreeNode):
        stack, res = [], []
        if root is None:
            return
        stack.append(root)
        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)

        return res[::-1]


