import random

results = []

for _ in range(10000):
    # Cycle: A->B->C->A
    # All 3 objects are in one cycle and will be collected
    # Order of deletion is implementation-defined
    group = ['A', 'B', 'C']
    random.shuffle(group)
    results.append("\n".join(f"Deleting {x}" for x in group))

print(results)