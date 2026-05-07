from scipy.stats import f

d1 = 1.3
d2 = 1.1
samples = []

for _ in range(10000):
    sample = f.rvs(dfn=d1, dfd=d2)
    samples.append(float(sample))

print(samples)
