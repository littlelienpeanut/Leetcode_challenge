class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        cnt = 0
        while x/2.0 > 0 or y/2.0 > 0:
            if (x % 2.0 == 0 and y % 2.0 == 0) or (x % 2.0 == 1 and y % 2.0 == 1):
                pass
            else:
                cnt += 1

            x = int(x / 2)
            y = int(y / 2)

        return cnt
                
