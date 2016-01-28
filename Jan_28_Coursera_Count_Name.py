# Old version
counts = dict()
names = ['Vlad', 'Serg', 'Sasha', 'Serg', 'Igor', 'Vlad', 'Bogdan']

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1

print counts

"""for name in names:
    print name, counts.get(name, 0)"""

# Upgrade

counts = dict()
names = ['Vlad', 'Serg', 'Sasha', 'Serg', 'Igor', 'Vlad', 'Bogdan']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print
print counts


# Upgrade 2
print({name:names.count(name) for name in names})