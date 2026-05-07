import numpy as np

labels = np.array([1, 2, 3, 4, 5, 6, 7, 8])
weights = np.array([0.12, 0.13, 0.11, 0.14, 0.10, 0.15, 0.12, 0.13])

outcomes = []
for _ in range(10000):
    outcome = np.random.choice(labels, p=weights)
    outcomes.append(int(outcome))

print(outcomes)
