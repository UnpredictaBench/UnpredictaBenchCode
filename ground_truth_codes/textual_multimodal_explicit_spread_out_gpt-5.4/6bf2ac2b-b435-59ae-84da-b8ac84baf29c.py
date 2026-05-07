import numpy as np

results = []

for _ in range(10000):
    weights = [0.5, 0.5]
    chosen = np.random.choice([0, 1], p=weights)

    if chosen == 0:
        x0 = 3
        probs = [0.70, 0.18, 0.12]  # [failure, type1, type2]
    else:
        x0 = 11
        probs = [0.40, 0.32, 0.28]  # [failure, type1, type2]

    counts = np.array([0, 0, 0])
    failures = 0
    while failures < x0:
        outcome = np.random.choice([0, 1, 2], p=probs)
        counts[outcome] += 1
        if outcome == 0:
            failures += 1

    X1, X2 = counts[1], counts[2]
    S = X1 + X2
    results.append(int(S))  # Ensure the value is a standard Python int

print(results)
