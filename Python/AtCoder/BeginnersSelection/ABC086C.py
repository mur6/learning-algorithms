import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
n = lines.pop(0)
prev_t = 0
prev_x = prev_y = 0
ok = True
for s in lines:
    t, x, y = map(int, s.split(" "))
    time = t - prev_t
    distance = abs(prev_x - x) + abs(prev_y - y)
    k = time - distance
    if k < 0:
        ok = False
        break
    if k % 2 == 0:
        prev_t, prev_x, prev_y = t, x, y
        continue
    else:
        ok = False
        break

if ok:
    print("Yes")
else:
    print("No")
