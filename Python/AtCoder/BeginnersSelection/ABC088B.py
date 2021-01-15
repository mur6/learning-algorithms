import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
n = lines.pop(0)
a_list = [int(n) for n in lines[0].split(" ")]
a_list.sort(reverse=True)
# print(a_list)
S = 0
for j, a in enumerate(a_list):
    if j % 2 == 0:
        S += a
    else:
        S -= a
print(S)
