import sys
line = [s.rstrip("\n") for s in sys.stdin.readlines()][0]
n, k = [int(n) for n in line.split(" ")]

def f(n, k):
    #if n == k:
    #    return 0
    while True:
        dif = abs(k - n)
        if  n > dif:
            p = n // k
            n = min(abs(n - p * k), abs(n - p * (k + 1)))
            #n = dif
        else:
            break
    return n

ans = f(n, k)
print(ans)
# if j <= k:
#     print("Yes")
# else:
#     print("No")
