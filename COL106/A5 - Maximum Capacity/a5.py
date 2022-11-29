from math import floor
from collections import deque

def findMaxCapacity(n, eds, s, t):

    if s == t:
        return ["INF", [s]]
    ad = [[] for _ in range(n)]
    r = 0
    for ed in eds:
        ad[ed[0]].append([ed[1], ed[2]])
        ad[ed[1]].append([ed[0], ed[2]])
        r = max(r, ed[2])
    l = 0
    r += 1

    path = []

    while l < r:
        mid = floor((l+r)/2)
        q = deque()
        par = [-1 for _ in range(n)]
        par[s] = s
        q.append(s)
        while q:
            u = q.popleft()
            if u == t:
                break
            for y in ad[u]:
                if y[1] < mid or par[y[0]] >= 0:
                    continue
                par[y[0]] = u
                q.append(y[0])
        if par[t] < 0:
            r = mid
        else:
            l = mid + 1
            path = [t]
            while not par[path[-1]] == path[-1]:
                path.append(par[path[-1]])

    return (l-1, path[::-1])


def convert(list):
    return tuple(i for i in list)

f = open("./hidden_testcase_12.txt","r")
n = [int(x) for x in next(f).split()]

links = []
for line in f:
    lst = [int(x) for x in line.split()]
    links.append(convert(lst))

s = links[-2]
t = links[-1]
n = n[0]
s = s[0]
t = t[0]
links.pop()
links.pop()
print(findMaxCapacity(n,links,s,t))