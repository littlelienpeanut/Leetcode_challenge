class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, sum(nums)
        
        
        for i in range(len(nums)):
            r -= nums[i]
            if r == l:
                return i
            l += nums[i]
        
        return -1
