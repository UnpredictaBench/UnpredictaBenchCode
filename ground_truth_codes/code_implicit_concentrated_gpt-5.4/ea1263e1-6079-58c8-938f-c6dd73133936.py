import numpy as np

a = 120.0
b = 140.0

samples = []

for _ in range(10000):
    u = np.random.chisquare(df=a)
    v = np.random.chisquare(df=b)
    sample = (u / a) / (v / b)
    samples.append(float(sample))

print(samples)
