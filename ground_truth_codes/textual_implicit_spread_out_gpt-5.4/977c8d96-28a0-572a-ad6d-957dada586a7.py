from scipy.stats import hypergeom

N = 120  # population size
K = 58   # number of success states in the population
n = 54   # number of draws without replacement

samples = []

for _ in range(10000):
    sample = hypergeom.rvs(M=N, n=K, N=n)
    samples.append(sample)

print(samples)
