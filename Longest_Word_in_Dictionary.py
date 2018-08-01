class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        w_dict = {}
        word_l = []
        word_set = set(words)
        for word in words:
            w_dict.update({word:len(word)})
            word_l.append(len(word))
        
        word_l = sorted(set(word_l), reverse=True)
        

        for i in word_l:
            output = []
            for word, length in w_dict.items():
                if length == i:
                    flag = 0
                    for c in range(len(word)):
                        if word[:c+1] not in word_set:
                            flag = 1
                            break
                    
                    if flag == 0:
                        output.append(word)
            
            if output != []:
                return min(output)
        
        
        
