val1 = 0
val2 = 0

for k in range(1,101):
    val1 += k ** 2
    val2 += k
val2 = val2 ** 2

print(val2-val1)

