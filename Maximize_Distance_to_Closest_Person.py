class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        begin = mid = end = cnt = 0
        begin = seats.index(1)
        end = seats[::-1].index(1)
        for i in seats:
            if i == 1:
                mid = max((cnt+1)//2, mid)
                cnt = 0
            else:
                cnt += 1
        
        return max(begin, mid, end)
                
