import sys
import math
lines = list(s.rstrip("\n") for s in sys.stdin)
input = int(lines[0])
ceiled = math.ceil(input / 1000.0)
answer = ceiled * 1000 - input
print(answer)
