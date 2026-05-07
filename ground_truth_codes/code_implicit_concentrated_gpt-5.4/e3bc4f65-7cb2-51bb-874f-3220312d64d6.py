import numpy as np

total_items = 18
special_items = 2
picked_items = 3

box = np.array([1] * special_items + [0] * (total_items - special_items))
results = []

for _ in range(10000):
    rng = np.random.default_rng()
    chosen = rng.choice(box, size=picked_items, replace=False)
    result = int(chosen.sum())
    results.append(result)

print(results)
