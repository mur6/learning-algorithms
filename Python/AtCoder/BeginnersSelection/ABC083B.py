import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
N, a, b = [int(n) for n in lines[0].split(" ")]
S = 0
for i in range(1, N + 1):
    p = sum(int(ch) for ch in str(i))
    if a <= p and p <= b:
        S += i
        #print(i, p)
print(S)
