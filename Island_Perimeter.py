class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cnt = 0
        grid.insert(0, [0]*(len(grid[0])+2))
        grid.append([0]*(len(grid[1])+2))

        for i in range(1, len(grid)-1, 1):
            grid[i].insert(0, 0)
            grid[i].append(0)

        for i in range(1, len(grid)-1, 1):
            for j in range(1, len(grid[i])-1, 1):
                if grid[i][j] == 1:
                    if grid[i-1][j] == 0:
                        cnt += 1

                    if grid[i][j-1] == 0:
                        cnt += 1

                    if grid[i+1][j] == 0:
                        cnt += 1

                    if grid[i][j+1] == 0:
                        cnt += 1
        return cnt
