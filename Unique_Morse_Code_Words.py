class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        letters = {'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".", 'f':"..-.", 'g':"--.", 'h':"....", 'i':"..", 'j':".---", 'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.", 'o':"---", 'p':".--.", 'q':"--.-", 'r':".-.", 's':"...", 't':"-", 'u':"..-", 'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--.."}


        morse_word = []
        count = 0

        for word in words:
            tmp_morse = ''
            for letter in range(len(word)):
                tmp_morse += letters[word[letter]]

            if tmp_morse in morse_word:
                pass
            else:
                count += 1
                morse_word.append(tmp_morse)

        return count
