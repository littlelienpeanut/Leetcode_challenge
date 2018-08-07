class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp_nums = list(set(nums))
        tmp_nums_2 = list(range(1, len(nums)+1))
        re = sum(nums) - sum(tmp_nums)
        mi = sum(tmp_nums_2) - sum(tmp_nums)
        return [re, mi]
                
        
