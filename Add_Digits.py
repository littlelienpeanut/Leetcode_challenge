class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        def add_digit(n):
            if len(str(n)) == 1:
                return n

            else:
                tmp = 0
                for d in str(n):
                    tmp += int(d)
                return add_digit(tmp)

        return add_digit(num)
