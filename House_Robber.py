class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fir = sec = 0
        
        for num in nums:
            fir, sec = sec, max(sec, fir+num)
        
        return max(fir, sec)
                
