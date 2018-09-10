# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.output = 0
        if not root:
            return self.output
        
        def dfs(root):
            if root.left and (not root.left.left and not root.left.right):
                self.output += root.left.val
            if root.left: dfs(root.left)
            if root.right: dfs(root.right)
        dfs(root)       
        return self.output
        
