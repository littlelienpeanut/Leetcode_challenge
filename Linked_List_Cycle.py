# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            slow = head
            fast = slow.next
            while (fast and slow):
                if slow.val == fast.val:
                    return True

                slow = slow.next
                fast = fast.next.next
        
            return False
        
        except:
            return False
