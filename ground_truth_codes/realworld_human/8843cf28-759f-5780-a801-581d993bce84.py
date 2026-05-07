import random
 
results = []
 
for _ in range(10000):
    combined = ["parent", "child"]
    random.shuffle(combined)
    results.append("\n".join(combined))
 
print(results)
 