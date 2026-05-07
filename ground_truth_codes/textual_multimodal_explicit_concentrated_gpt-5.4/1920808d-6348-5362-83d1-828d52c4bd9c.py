import numpy as np
from scipy.stats import chi2

weights = [0.5, 0.5]
components = [
    {
        'mu': np.array([0.0, 0.0]),
        'Sigma': np.array([[0.04, 0.0], [0.0, 0.04]]),
        'nu': 8
    },
    {
        'mu': np.array([1.2, 1.2]),
        'Sigma': np.array([[0.04, 0.0], [0.0, 0.04]]),
        'nu': 8
    }
]

samples = []

for _ in range(10000):
    k = np.random.choice([0, 1], p=weights)
    mu = components[k]['mu']
    Sigma = components[k]['Sigma']
    nu = components[k]['nu']

    y = np.random.multivariate_normal(mean=np.zeros(2), cov=Sigma)
    u_sample = chi2.rvs(df=nu)
    x = mu + y * np.sqrt(nu / u_sample)
    samples.append(float(x[0]))

print(samples)
