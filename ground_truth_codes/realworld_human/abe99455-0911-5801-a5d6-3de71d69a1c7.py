import random
 
results = []
 
# current = 0, so transition row is [0.2, 0.5, 0.3]
states = ["A", "B", "C"]
probs = [0.2, 0.5, 0.3]
 
for _ in range(10000):
    results.append(random.choices(states, weights=probs)[0])
 
print(results)
 