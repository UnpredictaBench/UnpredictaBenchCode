import numpy as np

population_size = 120
flagged_items = 58
items_checked = 67

urn = np.array([1] * flagged_items + [0] * (population_size - flagged_items))
results = []

for _ in range(10000):
    chosen = np.random.choice(urn, size=items_checked, replace=False)
    result = int(chosen.sum())
    results.append(result)

print(results)
