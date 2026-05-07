import numpy as np

x0 = 7
p = np.array([0.24, 0.21, 0.27])
p0 = 0.28
probs = np.append(p, p0)
sampled_values = []
rng = np.random.default_rng()

for _ in range(10000):
    failures = 0
    counts = np.zeros(3, dtype=int)
    while failures < x0:
        outcome = rng.choice(4, p=probs)
        if outcome == 3:
            failures += 1
        else:
            counts[outcome] += 1
    sample_x1 = int(counts[0])
    sampled_values.append(sample_x1)

print(sampled_values)
