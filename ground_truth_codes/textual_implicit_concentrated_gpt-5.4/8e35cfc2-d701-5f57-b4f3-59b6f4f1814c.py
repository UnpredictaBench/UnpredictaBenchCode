from scipy.stats import hypergeom

N = 24  # population size
K = 2   # number of defective chips (success states)
n = 3   # number drawn without replacement

samples = []
for _ in range(10000):
    sample = hypergeom.rvs(M=N, n=K, N=n)
    samples.append(sample)

print(samples)
