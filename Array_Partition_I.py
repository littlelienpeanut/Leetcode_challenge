class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nums = sorted(nums)
        for i in range(0, len(nums), 2):
            res += nums[i]

        return res
