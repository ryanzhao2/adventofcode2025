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
    
    arr = []
    #merge intervals
    for line in ranges.splitlines():
        x, y = map(int, line.split('-'))
        arr.append([x, y])

    arr.sort()
    ans = [arr[0]]
    for i in range(len(arr)):
        if arr[i][0] <= ans[-1][1]:
            ans[-1][1] = max(arr[i][1], ans[-1][1])
        else:
            ans.append(arr[i])
    
    res = 0
    for x, y in ans:
        res += (y - x) + 1


    print(res)


if __name__ == '__main__':
    solve()
