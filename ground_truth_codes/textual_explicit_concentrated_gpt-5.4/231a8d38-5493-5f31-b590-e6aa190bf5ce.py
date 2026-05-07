from scipy.stats import chi2

k = 1
samples = []

for _ in range(10000):
    sample = chi2.rvs(df=k)
    samples.append(float(sample))  # Convert np.float64 to regular float

print(samples)
