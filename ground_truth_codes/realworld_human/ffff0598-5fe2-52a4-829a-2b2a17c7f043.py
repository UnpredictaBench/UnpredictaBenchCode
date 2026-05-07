import random
 
results = []
 
states = ["validate_input", "retry_request", "escalate_issue"]
 
for _ in range(10000):
    results.append(random.choice(states))
 
print(results)