string = "Hibiscus moscheutos, commonly known by various names including rose mallow and swamp rose-mallow, is a species of flowering plant in the family Malvaceae. It is a cold-hardy perennial wetland plant that can grow in large colonies. The hirsute leaves are of variable morphology, but are commonly deltoidal in shape with up to three lobes. It is found in wetlands and along the riverine systems of the eastern United States from Texas to the Atlantic states, its territory extending northward to southe"

i = -1
res = ""

while i >= len(string) * -1:
    res = res + string[i]
    i = i - 1

print(res)
