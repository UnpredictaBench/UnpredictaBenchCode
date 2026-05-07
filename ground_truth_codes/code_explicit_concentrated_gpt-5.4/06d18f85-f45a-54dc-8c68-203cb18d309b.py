import numpy as np

# degrees of freedom
k = 1

samples = []

for _ in range(10000):
    # draw a single random sample from a chi-squared distribution
    sample = np.random.chisquare(df=k)
    samples.append(sample)

print(samples)
