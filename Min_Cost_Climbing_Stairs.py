class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        pre, cur = cost[0], cost[1]
        for i in range(2, len(cost), 1):
            pre, cur = cur, min(pre, cur) + cost[i]
        
        return min(pre, cur)
        
