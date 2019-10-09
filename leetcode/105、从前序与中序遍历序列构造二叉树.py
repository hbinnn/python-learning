"""
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder =?[3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 首先，preorder 中的第一个元素一定是树的根，这个根又将 inorder 序列分成了左右两棵子树。现在我们只需要将先序遍历的数组中删除根元素，
# 然后重复上面的过程处理左右两棵子树。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        pre_idx = 0
        idx_map = {val: idx for idx, val in enumerate(inorder)}

        def help(in_left=0, in_right=len(inorder)):
            nonlocal pre_idx

            if in_left == in_right:
                return None
            # preorder中的第一个元素作为树根
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            # 树根在inorder中的位置
            index = idx_map[root_val]
            # 下一树根
            pre_idx += 1
            # 递归构造左右子树
            root.left = help(in_left, index)
            root.right = help(index+1, in_right)
            return root

        return help()
