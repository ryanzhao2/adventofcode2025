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
    points = []
    for line in data:
        x, y = map(int, line.strip().split(','))
        points.append((x, y))

    ans = -1
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            ans = max(ans, (abs(x1-x2) + 1) * (abs(y1-y2) + 1))

    print(ans)




if __name__ == '__main__':
    solve()
