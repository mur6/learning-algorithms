import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
n, m = [int(num) for num in lines.pop(0).split(" ")]
day_to_price = {}
for d in range(1, m + 1):
    day_to_price[d] = set()
for _ in range(n):
    day, price = [int(num) for num in lines.pop(0).split(" ")]
    day_to_price[day].add(price)
print(day_to_price)

answer = 0
for day in range(1, m + 1):
    for d in range(day, 0, -1):
        if day_to_price[d]:
            price = max(day_to_price[d])
            answer += price
            day_to_price[d].remove(price)
            break
        else:
            continue

print(answer)
