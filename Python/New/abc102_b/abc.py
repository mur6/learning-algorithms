import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
n, = [int(num) for num in lines.pop(0).split(" ")]
a_list = [int(num) for num in lines.pop(0).split(" ")]
ans = max(a_list) - min(a_list)
print(ans)
