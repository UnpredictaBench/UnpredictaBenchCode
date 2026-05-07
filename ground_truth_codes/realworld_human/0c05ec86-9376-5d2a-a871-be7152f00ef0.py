import random
 
results = []
 
groups = [
    ("vowels", ['A', 'E', 'I']),
    ("consonants", ['B', 'C', 'D']),
    ("digits", ['1', '2', '3']),
]
 
for _ in range(10000):
    random.shuffle(groups)
    vowel = random.choice(['A', 'E', 'I'])
    consonant = random.choice(['B', 'C', 'D'])
    digit = random.choice(['1', '2', '3'])
    
    mapping = {"vowels": vowel, "consonants": consonant, "digits": digit}
    output = "\n".join(f"{name}: {mapping[name]}" for name, _ in groups)
    results.append(output)
 
print(results)