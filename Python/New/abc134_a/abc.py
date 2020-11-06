import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
r = int(lines.pop(0))
print(3 * r ** 2)
