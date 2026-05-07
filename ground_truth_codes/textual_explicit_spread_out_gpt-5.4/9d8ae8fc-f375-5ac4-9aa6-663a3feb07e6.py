from scipy.stats import chi2

k = 180
samples = []

for _ in range(10000):
    sample = chi2.rvs(df=k)
    samples.append(float(sample))  # Convert np.float64 to float

print(samples)
