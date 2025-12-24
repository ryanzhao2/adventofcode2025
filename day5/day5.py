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
    data = sys.stdin.read().strip()
    ranges, nums = data.split('\n\n')
    nums = map(int, nums.splitlines())
    r = []
    for line in ranges.splitlines():
        x, y = map(int, line.split('-'))
        r.append((x, y))

    ans = 0
    #print(nums)
    for val in nums:
        for x, y in r:
            if x <= val <= y:
                ans += 1
                break

    print(ans)

    
        

if __name__ == '__main__':
    solve()
