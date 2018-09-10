# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        s = []
        tmp = []
        diff = []
        
        while root or s:
            if root:
                s.append(root)
                root = root.right
            
            else:
                n = s.pop()
                tmp.append(n.val)
                root = n.left
        return min([abs(a-b) for a, b in zip(tmp, tmp[1:])])        
        
