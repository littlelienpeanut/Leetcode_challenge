import copy
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tmp_1, tmp_2 = nums[:], nums[:]
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                tmp_1[i] = nums[i+1]
                tmp_2[i+1] = nums[i]
                break
        
        return tmp_1 == sorted(tmp_1) or tmp_2 == sorted(tmp_2)
