import random

def searchNumInSortedList(num, lOrd):
    return searchNumInSortedList1(num, lOrd, 0, len(lOrd)-1)

def searchNumInSortedList1(num, lOrd, ini, fin):
    if(ini==fin):
        res = ini if num == lOrd[ini] else None
    else:
        media = int((ini + fin) / 2)
        elem = lOrd[media]
        res = searchNumInSortedList1(num, lOrd, ini, media) if num<=elem else searchNumInSortedList1(num, lOrd, media + 1, fin)
    return res

def calculaIndicesNumSortedList(num, lOrd):
    if(searchNumInSortedList(num, lOrd) == None):
        return (None, None)
    else:
        num_menor = num - 1
        num_mayor = num + 1
        resMenor = None
        while(resMenor == None or num_menor == 0):
            resMenor = searchNumInSortedList(num_menor, lOrd)
            num_menor-=1
        resMayor = None
        while(resMayor == None or num_mayor == 49):
            resMayor = searchNumInSortedList(num_mayor, lOrd)
            num_mayor+=1
        return(resMenor+1, resMayor-1)

l = []
num = 7
for i in range(50):
    l.append(random.randint(0, 50))
lOrd = sorted(l)
print("Sorted: ", lOrd)
print("Posición del número ", num, " es ", searchNumInSortedList(num, lOrd))
tup = calculaIndicesNumSortedList(num, lOrd)
print("Indices: ", tup)
print("El número", num, "se repite ", end = "")
if tup[1] == None:
    print("0 veces")
else:
    s = "veces"
    ve = tup[1] - tup[0] + 1
    if ve == 1:
        s = "vez"
    print(ve, s)
