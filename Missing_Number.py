class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = sum(nums)
        b = sum(range(len(nums)+1))
        return (b-a)
