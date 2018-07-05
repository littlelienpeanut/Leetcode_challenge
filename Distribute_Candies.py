class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        sis = int(len(candies)/2)

        if len(set(candies)) > sis:
            return sis

        else:
            return len(set(candies))
