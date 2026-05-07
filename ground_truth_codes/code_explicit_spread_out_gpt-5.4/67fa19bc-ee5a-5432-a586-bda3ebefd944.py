import numpy as np

k = 120
samples = []

for _ in range(10000):
    sample = np.random.chisquare(df=k)
    samples.append(sample)

print(samples)
