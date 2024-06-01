coordinates = [(5, 2), (13, 2), (15, -2), (15, 30)]

xs = []

i = 0

while i < len(coordinates):
    c = coordinates[i]
    xs.append(c[0])
    i = i + 1

print(min(xs), max(xs))
