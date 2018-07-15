class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        else:
            dict_s = {}
            dict_t = {}

            if set(s) != set(t):
                return False

            else:
                for i in set(s):
                    dict_s.update({i:0})
                    dict_t.update({i:0})

                for i in range(len(s)):
                    dict_s[s[i]] += 1
                    dict_t[t[i]] += 1

                for key in dict_s.keys():
                    if dict_s[key] != dict_t[key]:
                        return False

                return True
