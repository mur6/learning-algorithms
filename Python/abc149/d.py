import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
n, k = [int(n) for n in lines[0].split(" ")]
r, s, p = [int(n) for n in lines[1].split(" ")]
t = lines[2]
def won_it():
    for c in t:
        if c == "r":
            yield "p"
        elif c == "s":
            yield "r"
        elif c == "p":
            yield "s"
        else:
            assert False
w = list(won_it())
for i, c in enumerate(w):
    if k <= i:
        print(i, w[i - k], c)
print(f"{t}")
print(w)
