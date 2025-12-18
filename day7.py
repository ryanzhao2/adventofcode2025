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
    def dfs(r, c):
        if not isvalid(r, c) or (r, c) in visited:
            return 0
        visited.add((r, c))

        ans = 0
        if grid[r][c] == "S" or grid[r][c] == ".":
            ans += dfs(r + 1, c)

        elif grid[r][c] == "^":
            ans += dfs(r + 1, c - 1) + 1
            ans += dfs(r + 1, c + 1)

        return ans

    for i in range(n):
        if grid[0][i] == "S":
            print(dfs(0, i))



if __name__ == '__main__':
    solve()
