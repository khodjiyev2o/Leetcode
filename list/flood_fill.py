from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color: # if the starting pixel already has the new color, no need to perform flood fill
            return image
    
        def dfs(r, c, oldColor):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != oldColor:
                return
            image[r][c] = color # change color of current pixel
            dfs(r+1, c, oldColor) # dfs on bottom pixel
            dfs(r-1, c, oldColor) # dfs on top pixel
            dfs(r, c+1, oldColor) # dfs on right pixel
            dfs(r, c-1, oldColor) # dfs on left pixel
    
        dfs(sr, sc, image[sr][sc])
        return image

def test_floodFill():
    s = Solution()
    
    image1 = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ]
    sr1, sc1, color1 = 1, 1, 2
    assert s.floodFill(image1, sr1, sc1, color1) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    
    image2 = [
        [0, 0, 0],
        [0, 1, 1]
    ]
    sr2, sc2, color2 = 1, 1, 1
    assert s.floodFill(image2, sr2, sc2, color2) == [[0, 0, 0], [0, 1, 1]]
    
    image3 = [
        [0, 0, 0],
        [0, 0, 0]
    ]
    sr3, sc3, color3 = 0, 0, 1
    assert s.floodFill(image3, sr3, sc3, color3) == [[1, 1, 1], [1, 1, 1]]
    
    print("All test cases passed!")

test_floodFill()
