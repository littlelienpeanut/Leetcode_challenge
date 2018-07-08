class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = set()
        for n in nums:
            if n in tmp:
                tmp.remove(n)

            else:
                tmp.add(n)

        return tmp.pop()

        
