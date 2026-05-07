import random

my_list = ["forth", "second", "first", "third"]

results = []

for _ in range(10000):
    shuffled = my_list.copy()
    random.shuffle(shuffled)
    results.append(shuffled)

print(results)