class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid: return 0
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        for r in range(rows):
            for c in range(cols):
                if obstacleGrid[r][c] == 0:
                      # 初始起点为1(如果没有障碍物的情况下)
                    if r == 0 and c == 0: obstacleGrid[r][c] = 1
                    else:
                        left = obstacleGrid[r][c - 1] if c > 0 else 0
                        up = obstacleGrid[r - 1][c] if r > 0 else 0
                        obstacleGrid[r][c] = left + up
                else: obstacleGrid[r][c] = 0
        return obstacleGrid[rows - 1][cols - 1]