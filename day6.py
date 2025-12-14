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
    arr = []
    data = sys.stdin.read().splitlines()
    for line in data:
        arr.append(line.split())

    ans = 0
    for i in range(len(arr[0])):
        curr = int(arr[0][i])
        for j in range(1, len(arr)-1):
            #op is arr[-1][i]
            if arr[-1][i] == "*":
                curr = int(arr[j][i]) * int(curr)
            else:
                curr = int(arr[j][i]) + curr

        ans += curr

    print(ans)



if __name__ == '__main__':
    solve()
