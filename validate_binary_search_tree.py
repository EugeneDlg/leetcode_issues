# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root) -> bool:
        r = Solution.verify(root, None, -1000_000_000_000_000_000, 1000_000_000_000_000_000)
        return r

    @staticmethod
    def verify(node, parent, ancestor_left, ancestor_right):
        if node.left is not None:
            if node.left.val >= node.val:
                return False
            if parent is not None:
                if parent.right is not None:
                    if node.val == parent.right.val:
                        ancestor_left = parent.val
                if node.left.val <= ancestor_left:
                    return False
            r = Solution.verify(node.left, node, ancestor_left, ancestor_right)
            if not r:
                return False

        if node.right is not None:
            if node.right.val <= node.val:
                return False
            if parent is not None:
                if parent.left is not None:
                    if node.val == parent.left.val:
                        ancestor_right = parent.val
                if node.right.val >= ancestor_right:
                    return False
            return Solution.verify(node.right, node, ancestor_left, ancestor_right)
        return True