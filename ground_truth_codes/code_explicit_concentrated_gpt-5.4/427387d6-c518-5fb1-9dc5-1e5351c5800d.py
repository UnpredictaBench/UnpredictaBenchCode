import numpy as np

# Negative multinomial sampling via sequential categorical trials
# Stop when the number of failures (category 0) reaches x0.

x0 = 3
p = np.array([0.18, 0.12])   # success-category probabilities p1, p2
p0 = 1.0 - p.sum()            # failure probability

if x0 <= 0 or np.any(p < 0) or p0 <= 0:
    raise ValueError('Invalid negative multinomial parameters.')

probs = np.concatenate(([p0], p))
samples = []

for _ in range(10000):
    rng = np.random.default_rng()
    counts = np.zeros(len(p), dtype=int)
    failures = 0
    while failures < x0:
        outcome = rng.choice(len(probs), p=probs)
        if outcome == 0:
            failures += 1
        else:
            counts[outcome - 1] += 1
    samples.append(int(counts[0]))

print(samples)
