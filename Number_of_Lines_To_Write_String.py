class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        dict = {}
        output = [1, 0]
        tmp_line = 0

        letter = 'abcdefghijklmnopqrstuvwxyz'


        for i in range(len(S)):
            tmp_letter = letter.index(S[i])
            if tmp_line + widths[tmp_letter] > 100:
                output[0] += 1
                tmp_line = widths[tmp_letter]

            else:
                tmp_line += widths[tmp_letter]

        output[1] = tmp_line
        return output
