a = [
    "f10940jf1 49j1",
    "2039f2  1d1j0d9f1991 f",
    "20f1 1ed09j1ed22 9j1d11jj1",
    "0284h2083h20g",
    "208nv22djwfwsledif43",
    "20389fj203923vasdfvadv",
]


def sum_groups(string):
    i = 0
    holder = []
    temp_storage = ""

    while i < len(string):
        if string[i] in "1234567890":
            temp_storage = temp_storage + string[i]
        else:
            if temp_storage != "":
                holder.append(int(temp_storage))
                temp_storage = ""
        i = i + 1

    return sum(holder)


x = 0
total = 0
while x < len(a):
    line_sum = sum_groups(a[x])
    total += line_sum
    x = x + 1

print(total)
