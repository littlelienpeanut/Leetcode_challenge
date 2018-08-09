class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        pre = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[pre]:
                pre += 1
                nums[pre] = nums[i]
        
        return pre+1
