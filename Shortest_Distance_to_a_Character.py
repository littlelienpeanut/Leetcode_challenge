class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res = []
        for i in range(len(S)):
            if S[i] == C:
                res.append(0)
            else:
                MIN = 10000
                for j in range(len(S)):
                    if S[j] == C:
                        if j-i < MIN:
                            MIN = abs(j-i)
                        else:
                            pass

                    elif MIN < abs(j-i):
                        break

                    else:
                        pass
                res.append(MIN)

        return res
