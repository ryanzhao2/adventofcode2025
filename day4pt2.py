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
    #print(m, n)

    directions = [(1, 0), (0, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def valid(r, c):
        return 0 <= r < m and 0 <= c < m

    def check_box(r, c):
        total = 0

        for dx, dy in directions:
            nx, ny = r + dx, c + dy
            if valid(nx, ny) and grid[nx][ny] == "@":
                total += 1

        
        return total <= 3


    ans = 0
    while True:
        pos = []
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "@" and check_box(r, c):
                    pos.append((r, c))
        
        if not pos:
            break

        for (x, y) in pos:
            grid[x][y] = "."
            ans += 1
                
    print(ans)


if __name__ == '__main__':
    solve()
