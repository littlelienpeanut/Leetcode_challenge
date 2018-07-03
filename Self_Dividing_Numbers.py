class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        output = []
        for num in range(left, right+1, 1):
            tmp_num = str(num)
            for digit in range(len(tmp_num)):
                if int(tmp_num[digit]) == 0:
                    break

                elif num % int(tmp_num[digit]) != 0:
                    break

                elif digit == len(tmp_num) - 1:
                    if num % int(tmp_num[digit]) == 0:
                        output.append(num)

                else:
                    pass

        return output


        
