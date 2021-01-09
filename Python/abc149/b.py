import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
a, b, k = [int(n) for n in lines[0].split(" ")]
ans1 = max(a - k, 0)
if k >= a:
    ans2 = max(b - (k - a), 0)
else:
    ans2 = b
print(f"{ans1} {ans2}")
