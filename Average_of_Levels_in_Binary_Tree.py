# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        output = []
        
        if not root:
            return output
        
        remain = [root]
        
        while any(remain):
            tmp = []
            c = len(remain)
            cnt = 0
            while any(remain):
                curr = remain.pop(0)
                cnt += curr.val
                if curr.left: tmp += [curr.left]
                if curr.right: tmp += [curr.right]
            remain = tmp
            output.append(float(cnt)/c)
        
        return output
