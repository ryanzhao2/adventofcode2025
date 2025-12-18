#!/usr/bin/env python3
import sys
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
from functools import cache

MOD = 1000000007
INF = float('inf')

sys.setrecursionlimit(1000000)

# ---------------------- Solve Function ----------------------
def solve():
    grid = []
    data = sys.stdin.readlines()
    for line in data:
        grid.append(list(line.strip()))

    m, n = len(grid), len(grid[0])

    def isvalid(r, c):
        return 0 <= r < m and 0 <= c < n

    visited = set()

    @cache
    def dp(r, c):
        if not isvalid(r, c):
            return 0
        
        ans = 0
        if grid[r][c] == "S" or grid[r][c] == ".":
            ans += dp(r + 1, c)

        elif grid[r][c] == "^":
            ans += dp(r + 1, c - 1) + 1
            ans += dp(r + 1, c + 1)
        
        return ans

    for i in range(n):
        if grid[0][i] == "S":
            print(dp(0, i) + 1)



if __name__ == '__main__':
    solve()
