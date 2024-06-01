y = [1, 3, 0, 0, 2, 3, 4, 1, 0, 2, 5, 1, 0]

n = 0
i = 0

while i < len(y):
    if y[i] == 0:
        n = n + 1
    i = i + 1

print(n)