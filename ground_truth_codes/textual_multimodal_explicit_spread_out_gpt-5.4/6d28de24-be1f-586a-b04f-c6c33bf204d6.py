import numpy as np

weights = [0.5, 0.5]
degrees = [3, 30]
samples = []

for _ in range(10000):
    component = np.random.choice([0, 1], p=weights)
    sample = np.random.chisquare(df=degrees[component])
    samples.append(sample)

print(samples)
