num_set = set(range(1,10001))
generator = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    generator.add(i)

self_set = num_set - generator

for i in sorted(self_set):
    print(i)