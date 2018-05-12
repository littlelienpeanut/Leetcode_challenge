# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy = ListNode(0)
        current = dummy

        while l1 or l2 or carry:
            if l1:
                num_l1 = l1.val
                l1 = l1.next
            else:
                num_l1 = 0

            if l2:
                num_l2 = l2.val
                l2 = l2.next

            else:
                num_l2 = 0

            one = (num_l1 + num_l2 + carry) % 10
            carry = (num_l1 + num_l2 + carry) / 10
            current.next = ListNode(one)
            current = current.next

        return dummy.next
