import random

my_list = [1.26, 3.45, 4.78, 9.59]

results = []

for _ in range(10000):
    shuffled = my_list.copy()
    random.shuffle(shuffled)
    results.append(shuffled)

print(results)