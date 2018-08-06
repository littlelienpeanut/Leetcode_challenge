class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ind = 0
        while (ind < len(nums)):
            if target <= nums[ind]:
                return ind
            
            else:
                ind += 1
        
        return len(nums)
        
