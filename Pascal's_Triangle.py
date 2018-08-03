class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output = []
        for i in range(numRows):
            tmp = [1]*(i+1)
            if i > 1:
                for j in range(1, i):
                    tmp[j] = output[i-1][j-1]+output[i-1][j]
            
            output.append(tmp)
        
        return output
