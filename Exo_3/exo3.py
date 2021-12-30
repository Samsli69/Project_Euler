N = 600851475143

mylist = []
i = 2

while N != 0:

    if N % i == 0:
        N = N / i
        mylist.append(i)
        i = 2
    if N < i:
        break
    i = i + 1


for k in mylist:
    print(k)
