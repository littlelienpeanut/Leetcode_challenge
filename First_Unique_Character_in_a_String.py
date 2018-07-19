class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = set(list(s))
        output = []
        for ch in tmp:
            if s.count(ch) == 1:
                output.append(s.find(ch))

        if len(output) == 0:
            return -1

        else:
            return min(output)
