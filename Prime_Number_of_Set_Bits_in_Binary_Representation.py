class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        output = 0
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        for num in range(L, R+1, 1):
            tmp_num = bin(num)[2:]
            cnt = tmp_num.count('1')
            if cnt in prime:
                output += 1

        return output
            
