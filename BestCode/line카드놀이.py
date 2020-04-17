## template
import itertools
import sys

li = sys.stdin.readline().strip().split()
li = sorted(li)
k = int(sys.stdin.readline().strip())
p = list(map(' '.join,itertools.permutations(li)))
print(p[k-1])
