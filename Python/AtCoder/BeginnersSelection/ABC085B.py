import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
n = lines.pop(0)
d_list = set([int(n) for n in lines])
print(len(d_list))
