# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def pre(t):
            if not t:
                return ''
            
            c = str(t.val)
            l = pre(t.left)
            r = pre(t.right)
            if l == '' and r == '':
                return c
            
            elif l == '' and r:
                return c + '()(' + r + ')'
            
            elif l and r == '':
                return c + '(' + l + ')'
            
            else:
                return c + '(' + l + ')' + '(' + r + ')'
    
        return pre(t)
            
            
            
            
                
        
