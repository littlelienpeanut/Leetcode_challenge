"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        output, remain = [], [root]
        while any(remain):
            curr = remain.pop()
            output.append(curr.val)
            remain += [node for node in curr.children if curr]
        
        return output[::-1]
