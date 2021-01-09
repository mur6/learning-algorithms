import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
a, b = lines[0].split(" ")
print(f"{b}{a}")
