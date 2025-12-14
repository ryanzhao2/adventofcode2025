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
    """
    We want to check every column from right to left and see if its completely empty
    if its empty then we ignore it, otherwise we perform the operation on every value 
    from the rows of the column
    """


    t = []
    data = sys.stdin.read().splitlines()
    for line in data:
        t.append(line)
    
    ops = t[-1].split()[::-1]


    arr = []
    for val in t[:-1]:
        t2 = []
        for s in val:
            t2.append(s)

        arr.append(t2)

    empty = set()
    for col in range(len(arr[0])):
        check = False
        #keep track of columns that are empty
        for row in range(len(arr)):
            if arr[row][col] != ' ':
                check = True
        
        if not check:
            empty.add(col)

    ops_count = 0
    ans = 0
    total = []
    check2 = set()
    for col in range(len(arr[0])-1, -1, -1):
        s = ""
        for row in range(len(arr)):
            #check if col is empty and we perform op and skip
            if col in empty:
                #print(total)
                if ops[ops_count] == "*" and total != []:
                    ans += math.prod(total)
                elif ops[ops_count] == "+" and total != []:
                    ans += sum(total)

                if col not in check2:
                    check2.add(col)
                    ops_count += 1
                total = []

            else:
                v = arr[row][col]
                if v != " ":
                    s += v

        if s != "":
            total.append(int(s))


    #add the last
    if ops[ops_count] == "*":
        ans += math.prod(total)
    else:
        ans += sum(total)


    print(ans)
        















if __name__ == '__main__':
    solve()
