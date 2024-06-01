a = "ghw 323giu220834ghsx8fd8842 gfwwrg224f"

i = 0
holder = []
temp_storage = ""

while i < len(a):
    if a[i] in "1234567890":
        temp_storage = temp_storage + a[i]
    else:
        if temp_storage != "":
            holder.append(int(temp_storage))
            temp_storage = ""
    i = i + 1

print(sum(holder))
