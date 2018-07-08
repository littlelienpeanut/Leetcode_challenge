class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = S.split( )
        output = ''
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        for i in range(len(S)):
            if S[i][0] in vowel:
                output += (S[i] + 'ma' + 'a'*(i+1) + ' ')

            else:
                S[i] += S[i][0]
                output += (S[i][1:] + 'ma' + 'a'*(i+1) + ' ')

        return output[:-1]
        
