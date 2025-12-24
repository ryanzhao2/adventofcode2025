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
        line = line.strip().split(' ')
        indicator = line[0][1:-1]
        state = [0 if c == "." else 1 for c in indicator]
        
        #parse target into an integer
        target = 0
        for i, val in enumerate(state):
            if val == 1:
                target |= (1 << i)

        #parse buttons to integer marks to do bfs on
        btnmask = []
        for buttons in line[1:]:
            if buttons.startswith('('):
                indices = map(int, buttons[1:-1].split(','))
                mask = 0
                for idx in indices:
                    mask |= (1 << idx)

                btnmask.append(mask)

            else:
                break

        # BFS, initial state with no lights turned on and count = 0
        q = deque([(0, 0)])
        visited = {0}
        while q:
            curr, cnt = q.popleft()
            if curr == target:
                ans += cnt
                break
            
            for btn in btnmask:
                newmask = curr ^ btn
                if newmask not in visited:
                    visited.add(newmask)
                    q.append((newmask, cnt + 1))

    print(ans)


    

if __name__ == '__main__':
    solve()
