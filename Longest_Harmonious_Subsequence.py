from collections import Counter
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        num = Counter(nums)
        max_l = 0
        for key, value in num.items():
            if key+1 in num:
                tmp_l = num[key]+num[key+1]
                if tmp_l > max_l:
                    max_l = tmp_l
                    
        return max_l
        
            
