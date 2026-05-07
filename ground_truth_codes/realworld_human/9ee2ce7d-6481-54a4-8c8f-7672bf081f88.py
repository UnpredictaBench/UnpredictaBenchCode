import random
 
results = []
 
for _ in range(10000):
    # Equal chance of AB or BA, thread scheduling is unpredictable
    results.append(random.choice(["AB", "BA"]))
 
print(results)