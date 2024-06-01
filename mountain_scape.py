def mountain_scape(coords):
    visited = set()
    queue = [*coords]

    while queue:
        top = queue.pop()
        visited.add(top)
        x, y = top
        if y <= 1:
            continue
        n1 = (x + 1, y - 1)
        n2 = (x - 1, y - 1)
        queue.extend((n1, n2))
    
    print(visited)
    
    counter = 0
    
    for top in visited:
        if top[1] > 1:
            counter += 2
        else:
            counter += 1
    
    return counter

assert mountain_scape([(1, 1), (4, 2), (7, 3)]) == 13
assert mountain_scape([(0, 2), (5, 3), (7, 5)]) == 29
assert mountain_scape([(1, 3), (5, 3), (5, 5), (8, 4)]) == 37
print("Done")
