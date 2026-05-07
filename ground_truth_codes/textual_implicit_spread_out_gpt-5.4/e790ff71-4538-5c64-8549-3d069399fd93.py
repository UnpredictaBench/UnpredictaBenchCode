import numpy as np

x0 = 9
p = np.array([0.29, 0.31, 0.28])
p0 = 0.12
probs = np.append(p, p0)  # A, B, C, stop
counts = np.zeros(3, dtype=int)
failures = 0

samples = []

for _ in range(10000):
    while failures < x0:
        outcome = np.random.choice(4, p=probs)
        if outcome == 3:
            failures += 1
        else:
            counts[outcome] += 1

    sample = int(counts.sum())
    samples.append(sample)
    # Reset for next iteration
    counts = np.zeros(3, dtype=int)
    failures = 0

print(samples)
