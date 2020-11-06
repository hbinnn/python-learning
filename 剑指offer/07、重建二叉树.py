class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        pre_idx = 0
        idx_map = {val : idx for idx, val in enumerate(inorder)}

        def helper(in_left = 0, in_right = len(inorder)):
            nonlocal pre_idx

            if in_left == in_right:
                return None
            root = TreeNode(preorder[pre_idx])
            index = idx_map[preorder[pre_idx]]
            pre_idx += 1

            root.left = helper(in_left, index)
            root.right = helper(index, in_right)

            return root
        return helper()