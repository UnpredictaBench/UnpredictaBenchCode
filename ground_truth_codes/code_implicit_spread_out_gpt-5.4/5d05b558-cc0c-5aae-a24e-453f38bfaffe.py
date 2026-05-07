import numpy as np
from scipy.stats import norm, chi2

nu = 1.3
outcomes = []

for _ in range(10000):
    z = norm.rvs(loc=0, scale=1)
    v = chi2.rvs(df=nu)
    outcome = z / np.sqrt(v / nu)
    outcomes.append(float(outcome))

print(outcomes)
