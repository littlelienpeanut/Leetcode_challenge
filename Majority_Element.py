class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = list(set(nums))
        n_2 = len(nums) / 2
        dict = {}
        for num in s:
            dict.update({num:0})

        for n in nums:
            dict[n] += 1

        for num in dict.keys():
            if dict[num] > n_2:
                return num
