class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        def dfs(sr, sc):
            if len(image) > sr >= 0 and len(image[0]) > sc >= 0 and image[sr][sc] == ori_color:
                image[sr][sc] = newColor
                dfs(sr+1, sc)
                dfs(sr, sc+1)
                dfs(sr-1, sc)
                dfs(sr, sc-1)

            else:
                pass

        if image[sr][sc] == newColor:
            return image
        else:
            ori_color = image[sr][sc]
            dfs(sr, sc)
        return image
        
