from scipy.stats import t

nu = 30
samples = []

for _ in range(10000):
    sample = float(t.rvs(df=nu))
    samples.append(sample)

print(samples)
