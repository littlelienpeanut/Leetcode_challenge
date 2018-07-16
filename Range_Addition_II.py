class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """

        if ops == []:
            return m*n

        x = 40001
        y = 40001

        for i in range(len(ops)):
            if ops[i][0] < x:
                x = ops[i][0]

            if ops[i][1] < y:
                y = ops[i][1]

        return x*y
