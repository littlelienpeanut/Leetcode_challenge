from collections import Counter
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k > 0:
            tmp = set([n+k for n in nums])
            return len(set(nums)&set(tmp))
        
        elif k < 0:
            return 0
        
        else:
            return sum([val>1 for val in Counter(nums).values()])
            
            
