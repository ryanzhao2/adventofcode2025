#!/usr/bin/env python3
from enum import unique
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
        if not line.strip(): continue
        x, y = map(int, line.strip().split(','))
        points.append((x, y))

    #coordinate compression, we need an outside border for floodfill
    allx = [x for x, _ in points]
    ally = [y for _, y in points]

    xs = sorted(list(set(allx + [min(allx) - 1, max(allx) + 1])))
    ys = sorted(list(set(ally + [min(ally) - 1, max(ally) + 1])))

    #create a mapping
    x_map = {val : 2*i for i, val in enumerate(xs)}
    y_map = {val : 2*i for i, val in enumerate(ys)}

    #convert points to compressed points
    compressed_points = []
    for x, y in points:
        compressed_points.append((x_map[x], y_map[y]))

    #connect red points before and after in a staright line
    m, n = 2 * len(ys) - 1, 2 * len(xs) - 1
    grid = [[0] * n for _ in range(m)]
    npoints = len(compressed_points)
    for i in range(npoints):
        x1, y1 = compressed_points[i]
        x2, y2 = compressed_points[(i + 1) % npoints]
        if y1 == y2:
            start, end = min(x1, x2), max(x1, x2)
            for j in range(start, end + 1):
                grid[y1][j] = 1
            
        elif x1 == x2:
            start, end = min(y1, y2), max(y1, y2)
            for j in range(start, end + 1):
                grid[j][x1] = 1

    #floodfill inside
    def floodfill():
        visited = set()
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def valid(r,c):
            return 0 <= r < m and 0 <= c < n

        def dfs(r, c):
            if not valid(r, c) or grid[r][c] == 1 or (r, c) in visited:
                return

            grid[r][c] = 2
            visited.add((r, c))
            for dx, dy in dirs:
                nx, ny = r + dx, c + dy
                dfs(nx, ny)


        dfs(0, 0)

    floodfill()
    
    #after floodfill we want to set all the values inside of the rectangle to 1    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                grid[i][j] = 1


    #2d prefix sum
    prefix = [[0] * (n + 1) for _ in range(m + 1)]
    for r in range(m):
        for c in range(n):
            val = grid[r][c]
            #Inclusion-exclusion principle 
            prefix[r+1][c+1] = val + prefix[r][c+1] + prefix[r+1][c] - prefix[r][c]


    ans = 0
    for i in range(npoints):
        x1, y1 = points[i]
        cx1, cy1 = compressed_points[i]
        for j in range(i + 1, npoints):
            cx2, cy2 = compressed_points[j]
            x2, y2 = points[j]
            minx, miny, maxx, maxy = min(cx1, cx2), min(cy1, cy2), max(cx1, cx2), max(cy1, cy2)
            area = (abs(cx1 - cx2) + 1) * (abs(cy1 - cy2) + 1)
            # (A + B + C + D) - (A + B) - (A + C) + A = D (we want the rectangle D)
            area_sum = prefix[maxy+1][maxx+1] - prefix[miny][maxx+1] - prefix[maxy+1][minx] + prefix[miny][minx]
            if area == area_sum:
                real_area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
                ans = max(ans, real_area)

    print(ans)



        

        




if __name__ == '__main__':
    solve()
