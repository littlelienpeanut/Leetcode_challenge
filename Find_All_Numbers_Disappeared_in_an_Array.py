class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = set(range(1, len(nums)+1))
        return list(a - set(nums))
