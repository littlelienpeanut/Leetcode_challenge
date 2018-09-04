class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        tmp_nums = sorted(nums)
        if tmp_nums == nums:
            return 0
        
        l = r = flag = 0
        for i in range(len(nums)):
            if nums[i] != tmp_nums[i]:
                if flag == 0:
                    l = i
                    flag = 1
                r = i
        
        return r-l+1
