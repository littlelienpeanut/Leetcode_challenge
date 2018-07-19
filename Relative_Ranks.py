class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        medal = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(map(str, range(4, len(nums)+1, 1)))
        rank = sorted(nums, reverse=True)
        num2rank = dict(zip(rank, medal))
        for i in range(len(nums)):
            nums[i] = num2rank[nums[i]]
        return nums
