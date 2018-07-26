class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        tmp_s = []
        tmp_t = []
        for ch in S:
            if tmp_s and ch == '#':
                tmp_s.pop(len(tmp_s)-1)

            elif ch != '#':
                tmp_s.append(ch)

        for ch in T:
            if tmp_t and ch == '#':
                tmp_t.pop(len(tmp_t)-1)

            elif ch != '#':
                tmp_t.append(ch)


        return (tmp_s == tmp_t)
        
