words = [
    "flower",
    "flow",
    "flight",
]

i = 0

while i < 4:
    if words[0][i] == words[1][i] == words[2][i]:
        # H/W Print the letter itself if it is the same in all words
        print(i)
    i = i + 1
