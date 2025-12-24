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
    for line in data:

        bank = line.strip()
        arr = []
        i1 = -1
        for x in range(11, -1, -1):
            m1 = -1
            for i, val in enumerate(bank):

                if i >= i1 + 1 and int(val) > m1 and (len(bank) - i) > x:
                    m1 = int(val)
                    i1 = i      

    
            arr.append(str(m1))


        ans += int((''.join(arr)))


    print(ans)

    

if __name__ == '__main__':
    solve()
