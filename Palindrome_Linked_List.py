# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while (fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        
        pre = None
        while (slow):
            curr = slow
            slow = slow.next
            curr.next = pre
            pre = curr
        
        while (pre):
            if pre.val != head.val:
                return False
            
            pre = pre.next
            head = head.next
        
        return True
