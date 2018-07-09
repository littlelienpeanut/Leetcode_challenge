class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        cnt = 0
        # use pop is faster than remove
        while (cnt < len(nums)):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                cnt += 1

            else:
                i += 1
                cnt += 1
