class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        
        max_val = cur_val = nums[0]
        for num in nums[1:]:
            cur_val = max(num, cur_val + num)
            max_val = max(cur_val, max_val)
        
        return max_val
