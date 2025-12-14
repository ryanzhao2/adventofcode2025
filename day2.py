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
    nums = list((input().split(',')))
    ans = 0
    

    for val in nums:
        r1, r2 = map(int, val.split('-'))
        for n in range(r1, r2+1):
            l = len(str(n))
            v = str(n)
            #outer loop
            check = set()
            for i in range(1, l // 2 + 1):
                if l % i == 0:
                    flag = True
                    for j in range(i, l, i):
                        if v[j:j+i] != v[j-i:j]:
                            #print(v)
                            flag = False
                            break
                        else:
                            pass
                            #print(v, v[j:j+i], v[j-i:j])

                    if flag == True:
                        #print(flag, i, v, v[j:j+i], v[j-i:j])
                        #print(n)
                        if n not in check:
                            ans += n 
                        check.add(n)
    
    if ans >= 28196420717:
        print("TOO HIGH")

    print(ans)

if __name__ == '__main__':
    solve()

