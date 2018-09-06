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
        def LDR(root):
            if not root:
                return []
            
            else:
                if not root.left and not root.right:
                    return [root.val]
                
                else:
                    return LDR(root.left) + LDR(root.right)
        
        return LDR(root1) == LDR(root2)
                
