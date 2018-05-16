class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []

        for item in A:
            for i in range(len(item)):
                if item[i] == 0:
                    item[i] = 1
                else:
                    item[i] = 0

            result.append(item[::-1])


        return result
