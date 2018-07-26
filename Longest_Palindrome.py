from collections import Counter
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = Counter(s)
        cnt = 0
        mid_flag = 0
        for ch in d.keys():
            if d[ch] % 2 == 0:
                cnt += d[ch]

            else:
                cnt += (d[ch]-1)
                mid_flag = 1

        return (cnt + mid_flag)
