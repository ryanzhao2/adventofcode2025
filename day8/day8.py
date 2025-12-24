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

    #print(edges)
    
    c = 0
    for d, u, v in edges:
        c += 1
        if find(u) != find(v):
            union(u, v)
        if c == 1000:
            break

    groups = defaultdict(list)
    for i in range(len(boxes)):
        root = find(i)
        groups[root].append(i)

    sizes = [len(members) for members in groups.values()]
    sizes.sort(reverse=True)
    if len(sizes) > 2:
        print(sizes[0] * sizes[1] * sizes[2])

    


if __name__ == '__main__':
    solve()
