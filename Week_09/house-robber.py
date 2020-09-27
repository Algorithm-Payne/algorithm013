from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        size = len(nums)
        if size == 1: return nums[0]
        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, size):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[size - 1]


class Solution1:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        size = len(nums)
        if size == 1: return nums[0]
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, size):
            first, second = second, max(first + nums[i], second)
        return second
