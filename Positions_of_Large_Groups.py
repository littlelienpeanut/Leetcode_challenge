class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        ind = 1
        S = S + ','
        output = []
        cnt = 1
        first = S[0]
        while (len(S) > ind):
            if S[ind] == first:
                cnt += 1

            else:
                if cnt > 2:
                    tmp = [(ind-cnt), ind-1]
                    output.append(tmp)
                    cnt = 1
                    first = S[ind]

                else:
                    first = S[ind]
                    cnt = 1

            ind += 1

        return output
