arreter = False

N = 0
compteur = 0

while arreter == False:

    N = N + 1
    for k in range(1, 21):
        if N % k == 0:
            compteur = compteur + 1

        if compteur == 20:
            arreter = True
            break
    if compteur < 20:
        compteur = 0

print(N)
