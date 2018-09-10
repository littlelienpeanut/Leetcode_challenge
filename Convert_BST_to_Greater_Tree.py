# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        ori_r = root
        stack = []
        curr = 0
        
        while root or stack:
            if root:
                stack.append(root)
                root = root.right
            
            else:
                node = stack.pop()
                curr += node.val
                node.val = curr
                root = node.left
                
        return ori_r
                
