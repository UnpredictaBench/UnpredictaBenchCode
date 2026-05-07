import random
 
results = []
 
groups = [["A", "B"], ["1", "2"]]
 
for _ in range(10000):
    # Outer set order is random (no hashseed)
    shuffled_groups = random.sample(groups, len(groups))
    # Inner set item picked is also random
    output = "\n".join(random.choice(g) for g in shuffled_groups)
    results.append(output)
 
print(results)
 