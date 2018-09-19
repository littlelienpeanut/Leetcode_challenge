class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        output = []
        for i in range(left, right+1):
            flag = 0
            for num_i in str(i):
                if int(num_i) != 0 and i % int(num_i) == 0:
                    pass
                else:
                    flag = 1
                    break
            if flag == 0:
                output.append(i)
            
        
        return output
        
