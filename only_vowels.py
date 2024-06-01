string = "Some sentence"

vowels = {"a", "o", "i", "e", "u"}

i = 0
res = ""

while i < len(string):
    if string[i] in vowels:
        res = res + string[i]
    i = i + 1

print(res)
