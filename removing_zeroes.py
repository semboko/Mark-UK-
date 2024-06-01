def remove_zeros(numbers):
    r = []
    i = -1
    while i >= -len(numbers):
        if numbers[i] == 0:
            i -= 1
            continue
        r.append(numbers[i])
        i -= 1
    return r

print(remove_zeros([1, 5, 2, 0, 1, 0]))