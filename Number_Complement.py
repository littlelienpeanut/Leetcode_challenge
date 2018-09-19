class Solution:
    def findComplement(self, nums):
        """
        :type num: int
        :rtype: int
        """
        nums = bin(nums)[2:]
        output = ''
        for i in range(len(nums)):
            if nums[i] == '1':
                output += '0'
            
            else:
                output += '1'

        return int(output, 2)
                
        
        
