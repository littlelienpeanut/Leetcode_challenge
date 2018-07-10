class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        output = 0
        ori_bit = now_bit = s[0]
        cnt = {'0': 0, '1':0}
        bit = 0

        while (bit<(len(s))):
            if ori_bit != s[bit]:
                now_bit = s[bit]
                cnt[s[bit]] += 1
                bit += 1

            else:
                if now_bit != ori_bit:
                    output += min(cnt['0'], cnt['1'])
                    bit -= cnt[s[bit-1]]
                    cnt = {'0': 0, '1':0}
                    ori_bit = now_bit = s[bit]

                cnt[s[bit]] += 1
                bit += 1


        output += min(cnt['0'], cnt['1'])

        return output

        
