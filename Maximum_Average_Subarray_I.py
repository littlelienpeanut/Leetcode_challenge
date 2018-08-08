class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_val = tmp = sum(nums[:k])
        
        for i in range(len(nums)-k):
            tmp = tmp - nums[i] + nums[i+k]
            if tmp > max_val:
                max_val = tmp
        
        return max_val/float(k)
        
