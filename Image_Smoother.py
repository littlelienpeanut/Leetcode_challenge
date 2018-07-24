class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        new_M = [[0] * len(M[0]) for i in range(len(M))]
        def point(x, y):
            n = 0
            one = 0
            i = -1

            while (i<=1):
                j = -1
                while (j<=1):
                    if len(M) > (x+i) >= 0 and len(M[0]) > (y+j) >= 0:
                        n += 1
                        one += M[x+i][y+j]
                    
                    j += 1
                i += 1
            if n == 0:
                return 0
            else:
                return int(one/n)

        for i in range(len(M)):
            for j in range(len(M[i])):
                new_M[i][j] = point(i, j)

        return new_M
