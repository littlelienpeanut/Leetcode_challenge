class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        score = 0
        get_pt = []

        for pt in ops:
            if pt == 'C':
                score += get_pt[-1] * -1
                get_pt.pop(-1)

            elif pt == 'D':
                score += get_pt[-1] * 2
                get_pt.append(get_pt[-1] * 2)

            elif pt == '+':
                score += (get_pt[-1] + get_pt[-2])
                get_pt.append((get_pt[-1] + get_pt[-2]))

            else:
                score += int(pt)
                get_pt.append(int(pt))


        return score
