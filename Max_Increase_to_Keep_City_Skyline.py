class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        s_t = []
        s_l = []
        output = 0
        for i in range(len(grid)):
            s_l.append(max(grid[i]))
            max_val = 0
            for j in range(len(grid[i])):
                tmp = grid[j][i]
                max_val = max(tmp, max_val)
            s_t.append(max_val)
        
        for i in range(len(grid)):
            tmp_new_grid = []
            for j in range(len(grid[i])):
                tmp = min(s_t[j], s_l[i])
                tmp_new_grid.append(max(tmp, grid[i][j]))
            output += sum(tmp_new_grid) - sum(grid[i])
        
        return output
        
        
        
        
