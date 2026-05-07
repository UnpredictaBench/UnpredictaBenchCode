import numpy as np

weights = [0.5, 0.5]
dfs = [2, 8]
samples = []

for _ in range(10000):
    component = np.random.choice([0, 1], p=weights)
    sample = np.random.chisquare(df=dfs[component])
    samples.append(sample)

print(samples)
