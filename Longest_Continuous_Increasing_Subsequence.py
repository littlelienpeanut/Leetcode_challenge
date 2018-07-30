class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        
        output = 1
        ind = 1
        cnt = 1
        
        while (ind < len(nums)):
            if nums[ind] - nums[ind-1] > 0:
                cnt += 1
            
            else:
                cnt = 1
                
            ind += 1
            output = max(output, cnt)
        
        return output
            
        
