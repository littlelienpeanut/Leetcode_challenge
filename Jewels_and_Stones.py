class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        kind = {}
        for i in range(len(J)):
            if J[i] in kind.keys():
                pass

            else:
                kind.update({J[i]:0})

        for i in range(len(S)):
            if S[i] in kind.keys():
                count += 1



        return count
