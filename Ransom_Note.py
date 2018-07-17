class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for word in ransomNote:
            if magazine.find(word) == -1:
                return False

            else:
                magazine = magazine.replace(word, '', 1)

        return True
