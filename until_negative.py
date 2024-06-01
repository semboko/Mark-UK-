storage = []

while True:
    data = input()

    is_valid = True
    for char in data:
        if char not in "-0123456789":
            is_valid = False

    if not is_valid:
        print("Data contains a non-digit character. Try again")
        break

    storage.append(int(data))
    if int(data) < 0:
        print(sum(storage))
        exit()
