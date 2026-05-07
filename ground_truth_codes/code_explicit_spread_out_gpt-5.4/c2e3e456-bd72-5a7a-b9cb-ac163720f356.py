import numpy as np

# Negative multinomial sampling by simulating categorical trials
# until x0 failures (category 0) have occurred.

x0 = 7
p = np.array([0.18, 0.16, 0.21, 0.14])  # probabilities for categories 1..m
p0 = 1.0 - p.sum()                       # failure probability (category 0)

if x0 <= 0 or p0 <= 0 or np.any(p < 0):
    raise ValueError('Invalid negative multinomial parameters.')

probs = np.concatenate(([p0], p))
results = []

for _ in range(10000):
    counts = np.zeros(len(p), dtype=int)
    failures = 0
    while failures < x0:
        outcome = np.random.choice(len(probs), p=probs)
        if outcome == 0:
            failures += 1
        else:
            counts[outcome - 1] += 1
    results.append(int(sum(counts)))  # Convert np.int64 to int

print(results)
