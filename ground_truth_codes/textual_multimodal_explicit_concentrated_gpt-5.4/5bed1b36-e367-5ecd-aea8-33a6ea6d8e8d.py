import numpy as np

weights = [0.55, 0.45]
components = [
    {'x0': 2, 'p': [0.70, 0.18, 0.12]},
    {'x0': 2, 'p': [0.75, 0.05, 0.20]}
]

samples = []

for _ in range(10000):
    k = np.random.choice([0, 1], p=weights)
    x0 = components[k]['x0']
    p0, p1, p2 = components[k]['p']

    counts = [0, 0]
    failures = 0
    while failures < x0:
        outcome = np.random.choice([0, 1, 2], p=[p0, p1, p2])
        if outcome == 0:
            failures += 1
        else:
            counts[outcome - 1] += 1

    sample_value = counts[0] + counts[1]
    samples.append(sample_value)

print(samples)
