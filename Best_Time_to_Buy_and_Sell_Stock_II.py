class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        output = 0
        i = 0

        while (i<len(prices)):
            max_v = 0
            tmp_value = prices[i]
            for j in range(i, len(prices)-1, 1):
                if tmp_value > prices[j]:
                    break

                elif prices[j] > prices[j+1]:
                    max_v = prices[j] - tmp_value
                    i = j
                    break

                else:
                    max_v = prices[j+1] - tmp_value
                    i = j+1

            output += max_v
            i += 1

        return output
