# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.LDR(root1) == self.LDR(root2)
    
    def LDR(self, root):
        if not root:
            return []

        else:
            if not root.left and not root.right:
                return [root.val]

            else:
                return self.LDR(root.left) + self.LDR(root.right)
            
                
