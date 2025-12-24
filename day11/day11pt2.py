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

    memo = {}
    def dfs(curr, v1, v2):
        if curr == "out" and v1 and v2:
            return 1

        state = (curr, v1, v2)
        if state in memo:
            return memo[state]

        ans = 0
        for neighbor in adj[curr]:
            if neighbor == "fft":
                ans += dfs(neighbor, True, v2)
            elif neighbor == "dac":
                ans += dfs(neighbor, v1, True)
            else:
                ans += dfs(neighbor, v1, v2)

        memo[state] = ans
        return ans

    print(dfs("svr", False, False))



if __name__ == '__main__':
    solve()
