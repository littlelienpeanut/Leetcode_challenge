class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums)*len(nums[0]) < r*c:
            return nums

        else:
            output = []
            tmp_nums = []
            for i in range(len(nums)):
                tmp_nums.extend(nums[i])

            for ele in range(r):
                output.append(tmp_nums[ele*c:((ele+1)*c)])

            return output
