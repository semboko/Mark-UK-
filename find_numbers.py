a = "308n3048bn320483n4b"

i = 0
holder = []
while i < len(a):
    if a[i] in "1234567890":
        holder.append(int(a[i]))
    i = i + 1


print(sum(holder))
