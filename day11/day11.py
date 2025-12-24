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
    adj = defaultdict(list)
    for line in data:
        line = line.strip().split(' ')
        for val in line[1:]:
            adj[line[0][:-1]].append(val)
    
    def dfs(curr):
        if curr == "out":
            return 1

        ans = 0
        for neighbor in adj[curr]:
            ans += dfs(neighbor)

        return ans

    print(dfs("you"))


if __name__ == '__main__':
    solve()
