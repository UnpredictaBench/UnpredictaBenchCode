from scipy.stats import t

nu = 1.3
samples = []

for _ in range(10000):
    sample = float(t.rvs(df=nu))
    samples.append(sample)

print(samples)
