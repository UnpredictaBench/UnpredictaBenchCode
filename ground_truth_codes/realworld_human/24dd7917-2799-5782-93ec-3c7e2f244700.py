import random

results = []

for _ in range(10000):
    # 90% chance no race condition -> x = 2
    # 10% chance race condition -> x = 1
    if random.random() < 0.1:
        results.append(1)
    else:
        results.append(2)

print(results)