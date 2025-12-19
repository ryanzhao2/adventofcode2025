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


    parent = {}
    def find(x):
        if x not in parent:
            parent[x] = x
        if parent[x] != x:
            parent[x] = find(parent[x])  # path compression
        return parent[x]

    def union(x, y):
        parent[find(x)] = find(y)


    boxes = []
    data = sys.stdin.readlines()
    for line in data:
        x, y, z = list(map(int, line.strip().split(',')))
        boxes.append((x, y, z))
    

    #use kruskals algo
    edges = []
    for i in range(len(boxes)): 
        x1, y1, z1 = boxes[i]
        for j in range(i + 1, len(boxes)):
            x2, y2, z2 = boxes[j]
            dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
            edges.append((dist, i, j))

    edges.sort()

    last = -1
    for d, u, v in edges:
        if find(u) != find(v):
            last = boxes[u][0] * boxes[v][0]
            union(u, v)

        
    print(last)


    


if __name__ == '__main__':
    solve()
