class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        tmp = int(area**(1/2))
        while (tmp > 0):
            if area % tmp == 0:
                output = [int(area/tmp), tmp]
                return output

            tmp -= 1
            
