import sys

def iter(n):
    # 偶数なら、2で割る
    # 奇数なら、3倍して1を足す。
    while True:
        yield n
        if n == 1:
            break
        if n % 2 == 0:
            n //= 2
        else:
            n = (3 * n) + 1


n = int(sys.argv[1])
print(" ".join(map(str, iter(n))))
