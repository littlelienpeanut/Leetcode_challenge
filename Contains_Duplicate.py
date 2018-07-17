class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = list(set(nums))
        if len(nums) == len(n):
            return False

        else:
            return True
        
