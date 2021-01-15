import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
S = lines[0]

def parse(s):
    while True:
        if len(s) < 5:
            return False
        count = None
        if s.startswith("dreamerase"):
            count = 5
        elif s.startswith("dreamer"):
            count = 7
        elif s.startswith("dream"):
            count = 5
        elif s.startswith("eraser"):
            count = 6
        elif s.startswith("erase"):
            count = 5
        if count is None:
            return False
        s = s[count:]
        if len(s) == 0:
            return True

print("YES" if parse(S) else "NO")
