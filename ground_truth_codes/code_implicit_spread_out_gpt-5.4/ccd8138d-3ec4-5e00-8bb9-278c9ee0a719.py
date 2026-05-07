import numpy as np

rng = np.random.default_rng()
scale = 6.0
shape_tag = 5

values = []
for _ in range(10000):
    latent = rng.rayleigh(scale=scale)
    value = rng.gamma(shape=shape_tag, scale=latent / shape_tag)
    values.append(float(value))

print(values)
