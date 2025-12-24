#!/usr/bin/env python3
import sys
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
from functools import cache
import z3

MOD = 1000000007
INF = float('inf')

sys.setrecursionlimit(1000000)

# ---------------------- Solve Function ----------------------
def solve():
    data = sys.stdin.readlines()
    ans = 0
    for line in data:
        line = line.strip().split(' ')
        
    
        buttons = [] 
        #parse buttons and targets
        for part in line[1:]:
            if part.startswith('('):
                content = part[1:-1]
                indices = list(map(int, content.split(',')))
                buttons.append(indices)

            elif part.startswith('{'):
                content = part[1:-1]
                targets = list(map(int, content.split(',')))

        
        #use z3 library to solve and minimize linear equations
        opt = z3.Optimize()
        presses = [z3.Int(f'x_{i}') for i in range(len(buttons))]

        #constraint, all presses must be greater or equal to 0
        for val in presses:
            opt.add(val >= 0)


        for idx in range(len(targets)):
            #terms are x_1, x_2, x_3,...., x_n
            terms = []
            for i in range(len(buttons)):
                #only add the button if it affects the counter idx
                if idx in buttons[i]:
                    terms.append(presses[i])

            #we need to equate the equations to solve iff we have buttons to press
            if terms:
                opt.add(z3.Sum(terms) == targets[idx])
        
        total = z3.Sum(presses)
        opt.minimize(total)
        if opt.check() == z3.sat:
            ans += opt.model().eval(total).as_long()

    print(ans)


        

if __name__ == '__main__':
    solve()
