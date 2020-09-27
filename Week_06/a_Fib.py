from typing import Any, List

#  一维无限制DP

# 斐波那契数列
# 斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

# F(0) = 0, F(1) = 1
# F(N) = F(N - 1) + F(N - 2),
# 其中N > 1.
# 给定 N，计算 F(N)。

'''
# 法一：暴力递归:
1.由题意可知：F(0) = 0, F(1) = 1, F(N) = F(N - 1) + F(N - 2)，
逆推得起始条件：F(0) = 0, F(1) = 1,求F（N）-> F(N - 1) + F(N - 2)
2, 终止条件，处理当前层，dill down


# 法二 递归 + 减枝（缓存）
在法一的基础上加缓存实现剪枝，减少多余的重复运算

# 法三 数组DP
由题意可得：[F(0), F(1), F(1)+ F(0), F(1) + F(1) + F(0), ... F(N - 1) + F(N - 2)]
建立DP表，保存且保存，前两位

# 法四：DP
列出已知F(0) = 0, F(1) = 1, F(N) = F(N - 1) + F(N - 2)，
由F(N) = F(N - 1) + F(N - 2)，“未知”F（2）开始，补全。

# 法五：简化DP
直接拿到已知的动态转移方程DP
F(N) = F(N - 1) + F(N - 2)
# 法六： 数学黄金切割解斐波那契
'''


# 法一：暴力递归
class Solution1:
    def fib(self, N: int) -> int:
        if N < 2:
            return N
        return self.fib(N - 1) + self.fib(N - 2)


# 法二 递归 + 减枝（缓存）
class Solution2:
    from functools import lru_cache
    @lru_cache(maxsize=None)
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        else:
            return self.fib(N - 1) + self.fib(N - 2)


# 法三 数组DP
class Solution3:
    def fib(self, N: int) -> int:
        dp = [0] * N
        dp[0] = 0
        dp[1] = 1
        for i in range(3, N + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[N - 1]


# # 法四：DP
# class Solution4:
#     def fib(self, N: int) -> int:
#         curr, prev1, prev2 = 0, 1, 1
#         for i in range(3, N + 1):
#             curr = prev1 + prev2
#             prev2 = prev1
#             prev1 = curr
#         return curr


# 法五：简化DP
class Solution5:
    def fib(self, N: int) -> int:
        prev, now = 0, 1
        for i in range(N):
            prev, now = now, now + prev
        return prev


# 法六
class Solution6:
    def fib(self, N: int) -> int:
        sqrt5 = 5 ** 0.5
        fun = pow((1 + sqrt5) / 2, n + 1) - pow((1 - sqrt5) / 2, n + 1)
        return int(fun / sqrt5)
