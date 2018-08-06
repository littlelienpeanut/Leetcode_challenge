class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = digits[::-1]
        carr = 0
        digits[0] += 1
        for i in range(len(digits)):
            digits[i] += carr
            if digits[i] > 9:
                digits[i] -= 10
                carr = 1
            
            else:
                return digits[::-1]
        
        if carr == 1:
            digits.append(1)
        
        return digits[::-1]
        
        
