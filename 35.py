from itertools import permutations
import math

def eratosthenes(num):
    search = [i for i in range(2,num)]
    sosuu = []

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

    return sosuu



r_cnt = 0
sosuu = eratosthenes(1000000)
for i in range(1,1000000,2):
    s = str(i) + str(i)
    l = []
    #print(s)
    cnt = 0
    for j in range(int(len(str(s))/2)):
        if int(s[j:j+int(len(str(s))/2)]) not in sosuu:
            cnt += 1
            break
    if cnt == 0:
        r_cnt += 1
        print(i)
print(r_cnt)
