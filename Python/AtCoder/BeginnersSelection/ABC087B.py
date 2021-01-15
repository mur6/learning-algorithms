import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
a, b, c, x = [int(n) for n in lines]
cc_list = [a, b, c]
yen_list = [500, 100, 50]

def search(i, rest):
    if i == 3:
        if rest == 0:
            return 1
        else:
            return 0
    num = 0
    coin_count = cc_list[i]
    yen = yen_list[i]
    for j in range(coin_count):
        p = (j + 1) * yen
        if  p <= rest:
            num += search(i + 1, rest - p)
        else:
            break
    num += search(i + 1, rest)
    return num

ans = search(0, rest=x)
print(ans)
