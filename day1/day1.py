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
    ans = 0
    start = 50
    for line in data:
        line = line.strip()
        d = line[0]
        deg = int(line[1:])
        #print(deg)
        if d == "L":
            for i in range(start-1, start-deg-1, -1):
                if i % 100 == 0:
                    ans += 1

            start = (start - deg) % 100
        else:
            for i in range(start+1, start+deg+1):
                if i % 100 == 0:
                    ans += 1

            start = (start + deg) % 100


    print(ans)



if __name__ == '__main__':
    solve()
