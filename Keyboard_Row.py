class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        output = []
        row_1 = 'qwertyuiopQWERTYUIOP'
        row_2 = 'asdfghjklASDFGHJKL'
        row_3 = 'zxcvbnmZXCVBNM'

        for word in words:

            for i in range(len(word)):
                if i == 0:
                    if row_1.find(word[i]) != -1:
                        flag = 1

                    elif row_2.find(word[i]) != -1:
                        flag = 2

                    else:
                        flag = 3

                if row_1.find(word[i]) != -1:
                    if flag != 1:
                        flag = -1
                        break

                elif row_2.find(word[i]) != -1:
                    if flag != 2:
                        flag = -1
                        break

                else:
                    if flag != 3:
                        flag = -1
                        break

            if flag != -1:
                output.append(word)

        return output
