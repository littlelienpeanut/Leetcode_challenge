class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        output = [[1], [1, 1]]
        
        for i in range(rowIndex+1):
            if i > 1:
                tmp = []
                tmp.append(1)
                for j in range(1, i):
                    tmp.append(output[i-1][j-1] + output[i-1][j])
                
                tmp.append(1)
                output.append(tmp)
        
        return output[rowIndex]
