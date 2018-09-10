# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        tmp = []
        diff = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.right
                
            else:
                node = stack.pop()
                tmp.append(node.val)
                root = node.left
        
        for i in range(len(tmp)):
            for j in range(len(tmp)):
                if i == j:
                    pass
                else:
                    diff.append(abs(tmp[i] - tmp[j]))
            
        
        return min(diff)
