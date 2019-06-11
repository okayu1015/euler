import math
def eratosthenes(num):
    search = [i for i in range(2,num)]
    sosuu = []

    if num > 1000*1000:
        x = 1000
    else:
        x = int(math.sqrt(len(search)))
    i = 2
    while i <= x:
        sosuu.append(search[0])
        for j in range(2,num):
            if j % sosuu[-1] == 0 and j in search:
                search.remove(j)
        i += 1
    sosuu.extend(search)
    print(sosuu) #素数一覧
    print(len(sosuu)) #素数の個数

    return len(sosuu)

print(eratosthenes(1000000))
