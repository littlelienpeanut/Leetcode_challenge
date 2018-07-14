class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.lower()
        paragraph = paragraph.replace('!', '')
        paragraph = paragraph.replace('?', '')
        paragraph = paragraph.replace("'", '')
        paragraph = paragraph.replace(',', '')
        paragraph = paragraph.replace(';', '')
        paragraph = paragraph.replace('.', '')

        words = paragraph.split( )
        dict = {}
        max = 0

        for word in words:
            try:
                dict[word] += 1

            except:
                dict.update({word: 1})

        for word in banned:
            dict[word] = 0

        for key in dict.keys():
            if dict[key] > max:
                max = dict[key]
                output = key

        return output


        
