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
    data = sys.stdin.read()
    slots = {0: 7, 1: 7, 2: 7, 3: 7, 4: 5, 5: 6}
    ans = 0
    #box 0: 7, box 1: 7, box 2: 7, box 3: 7, box 4: 5, box 5: 6
    for line in data.splitlines():
        line = line.strip()
        if len(line) > 4:
            grid = line.split(' ') 
            w, l = int(grid[0][0:2]), int(grid[0][3:-1])
            size = w * l
            curr = 0
            vals = grid[1:]
            for v in range(len(vals)):
                curr += slots[v] * int(vals[v])
                
            if curr < size:
                ans += 1
            
            
    print(ans)
            

            

            


if __name__ == '__main__':
    solve()
