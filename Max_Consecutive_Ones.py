class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list = []
        nums.append(0)
        cnt = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                list.append(cnt)
                cnt = 0

            else:
                cnt += 1

        return max(list)
