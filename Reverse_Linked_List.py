# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = None
        output = None

        while (head != None):
            output = head
            head = head.next
            output.next = tmp
            tmp = output

        return output
