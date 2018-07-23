from collections import Counter
class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_r = nums[::-1]
        output = []
        a = Counter(nums)
        max_value = max(a.values())

        if max_value == 1:
            return 1


        for num, times in a.items():
            if times == max_value:
                first = nums.index(num)
                last = nums_r.index(num)
                output.append(((len(nums)-1 - last) - first + 1))

        return min(output)
