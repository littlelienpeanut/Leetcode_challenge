class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1:
            return True

        else:
            tmp_word = word.upper()
            if tmp_word == word:
                return True

            else:
                tmp_word = word.lower()
                if tmp_word[1:] == word[1:]:
                    return True

                else:
                    return False
