import random
 
results = []
 
for _ in range(10000):
    # Java GC with finalize() is non-deterministic:
    # - GC may or may not run
    # - finalize() may or may not be called
    # - order of finalization is random
    # - some or all objects may be finalized
 
    objects = ['A', 'B', 'C']
    
    # Chance that GC actually collects all, some, or none
    num_collected = random.choices([0, 1, 2, 3], weights=[0.25, 0.25, 0.25, 0.25])[0]
    collected = random.sample(objects, num_collected)
    random.shuffle(collected)
    
    results.append("\n".join(collected) if collected else "(no output)")
 
print(results)
 