from typing import List, Any


class Solution:
    def fib(self, N: int) -> int:
        dp = [0] * N
        dp[0] = 0
        dp[1] = 1
        for i in range(3, N + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[N - 1]


# 简化DP
class Solution1:
    def fib(self, N: int) -> int:
        prev, now = 0, 1
        for i in range(N):
            prev, now = now, now + prev
        return prev
