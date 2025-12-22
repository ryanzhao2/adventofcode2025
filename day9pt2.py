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
    data = sys.stdin.readlines()
    points1 = defaultdict(list)
    points2 = defaultdict(list)
    m = 0
    n = 0
    for line in data:
        x, y = map(int, line.strip().split(','))
        x -= 1
        y -= 1
        m = max(m, x)
        n = max(n, y)
        points1[x].append(y)
        points2[y].append(x)

    grid = [[0] * (m+1) for _ in range(n+1)]
    for c in points1.keys():
        small = 1000000
        large = 0
        for r in points1[c]:
            small = min(small, r)
            large = max(large, r)

        for i in range(small, large + 1):
            grid[i][c] = 1
        
    for r in points2.keys():
        small = 1000000
        large = 0
        for c in points2[r]:
            small = min(small, c)
            large = max(large, c)

        for i in range(small, large + 1):
            grid[r][i] = 1

    for v in points1.keys():
        for val in points1[v]:
            grid[val][v] = 2

    print(1)

    

        
            
    
    




if __name__ == '__main__':
    solve()
