cptNbrePremier = 0
nbre = 1
controle = False
while controle == False:
    nbre += 1

    if nbre == 2 or nbre == 3 or nbre == 5:
        cptNbrePremier += 1
        continue

    for i in range(2, nbre):
        if nbre % i == 0:
            break
        if i == nbre-1:
            cptNbrePremier += 1

    if cptNbrePremier == 10001:
        print(nbre)
        controle = True
