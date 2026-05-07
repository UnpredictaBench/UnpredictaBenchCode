import numpy as np
from scipy.stats import chi2

a = 2.3
b = 1.4
outcomes = []

for _ in range(10000):
    u = chi2.rvs(df=a)
    v = chi2.rvs(df=b)
    outcome = (u / a) / (v / b)
    outcomes.append(float(outcome))

print(outcomes)
