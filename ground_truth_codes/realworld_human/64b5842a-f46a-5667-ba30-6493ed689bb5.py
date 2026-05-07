import random
 
# MCMC samples from Normal(0,1)
# After burn-in, final sample is approximately Normal(0,1)
# P(x < 0) = 0.5, P(0 <= x < 1) ~= 0.341, P(x >= 1) ~= 0.159
 
results = []
 
for _ in range(10000):
    sample = random.gauss(0, 1)
    if sample < 0:
        results.append("A")
    elif sample < 1:
        results.append("B")
    else:
        results.append("C")
 
print(results)
 