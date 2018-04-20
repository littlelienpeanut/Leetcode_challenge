class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        tmp_x = abs(x)

        if x < 0:
            sign = -1

        else:
            sign = 1

        for i in range(len(str(tmp_x))):
           res += int(str(tmp_x)[i]) * math.pow(10, i)

        res = int(res) * sign


        if res > math.pow(2, 31) - 1 or res < -math.pow(2, 31):
            return 0

        else:
            return res
