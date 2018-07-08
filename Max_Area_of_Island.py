class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i, j):
            if len(grid) > i >= 0 and len(grid[0]) > j >= 0 and grid[i][j] == 1:
                # already visited set zero
                grid[i][j] = 0
                return (1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1))

            else:
                return 0

        max = 0

        for h in range(len(grid)):
            for v in range(len(grid[h])):
                tmp = dfs(h, v)
                if tmp > max:
                    max = tmp

        return max
