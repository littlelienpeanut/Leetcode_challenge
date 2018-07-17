class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)

        co_i = 0
        ch_i = 0

        while (ch_i < len(g) and co_i < len(s)):
            if g[ch_i] <= s[co_i]:
                ch_i += 1
                co_i += 1

            else:
                co_i += 1


        return ch_i




        
