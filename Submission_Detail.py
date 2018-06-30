class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        dict = {'U': 0, 'R': 0, 'D': 0, 'L': 0}

        for i in range(len(moves)):
            dict[moves[i]] += 1

        if dict['U'] == dict['D'] and  dict['R'] == dict['L']:
            return True

        else:
            return False
