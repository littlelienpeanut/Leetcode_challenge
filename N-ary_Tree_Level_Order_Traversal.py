"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        output = []
        if not root:
            return output
        
        remain = [root]
        while any(remain):
            tmp = []
            tmp_output = []
            while any(remain):
                curr = remain.pop(0)
                tmp_output.append(curr.val)
                tmp += [node for node in curr.children if curr]
            
            remain = tmp
            output.append(tmp_output)
        
        return output
