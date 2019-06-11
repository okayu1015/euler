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
    return sosuu

prime = eratosthenes(1000000)
prime.remove(2)
prime.remove(3)
prime.remove(5)
prime.remove(7)

s = '3797'
if int(s[1:]) in prime:
    print(s[1:])

sum = 0
for i in prime:
    s = str(i)
    cnt = 0
    while len(s) > 0:
        j = int(s[1:])
        if j in prime:
            s = s[1:]
            cnt += 1
        else:
            break
        
    s = str(i)
    l_cnt = 0
    while len(s) > 0:
        j = int(s[0:-1])
        if j in prime:
            s = s[0:-1]
            l_cnt += 1
        else:
            break
    if len(s) == cnt and len(s) == l_cnt:
        print(i)
        sum += i
print(sum)
