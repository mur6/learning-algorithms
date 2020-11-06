import sys, math
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
a, b, x = [int(n) for n in lines[0].split(" ")]
# print(a, b, x)

def get_max(target_number, digit):
    target_number_digit = len(str(target_number))
    if target_number_digit > digit:
        return int("9" * digit)
    elif target_number_digit == digit:
        return target_number
    else:
        return None

answer = 0
for d in range(1, 11):
    k = (x - b * d) / a
    if k <= 0.0:
        break
    m = get_max(math.floor(k), d)
    # print(f"k={k} m={m}")
    if m is None:
        break
    answer = m
if answer >= 1000000000:
    answer = 1000000000
print(answer)
