class Solution(object):
    def twoSum(self, nums, target):
        nums_sorted = sorted(nums)
        
        l = 0
        r = len(nums)-1
        
        while l < r:
            tmp = nums_sorted[l] + nums_sorted[r]
            if tmp == target:
                output_1 = nums.index(nums_sorted[l])
                nums[output_1] = None
                output_2 = nums.index(nums_sorted[r])
                return [output_1, output_2]
            
            if tmp > target:
                r -= 1
            
            else:
                l += 1
        
