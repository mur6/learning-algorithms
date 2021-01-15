import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
N, yen = [int(n) for n in lines[0].split(" ")]
res = yen - 1000 * N
ok = None
for i in range(N + 1):
    for j in range(N - i + 1):
        a2 = 9000 * i + 4000 * j
        if res == a2:
            #print(i, j, a2)
            ok = (i, j, N - i - j)
            break
if ok:
    x, y, z = ok
    print(f"{x} {y} {z}")
else:
    print("-1 -1 -1")
