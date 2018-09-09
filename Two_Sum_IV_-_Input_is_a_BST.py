# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        nums, remain = set(), [root]
        while remain:
            curr = remain.pop(0)
            nums.add(curr.val)
            if curr.left: remain += [curr.left]
            if curr.right: remain += [curr.right]
        
        for n in nums:
            nums.remove(n)
            if k-n in nums:
                return True
            nums.add(n)
        
        return False
