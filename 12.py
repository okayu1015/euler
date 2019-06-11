def sosuu_cnt(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    return cnt
    

p = []
i = 1
s = 1


while sosuu_cnt(s) < 500:
    p.append(i)
    s =sum(p)
    print(str(s) + ':' +str(sosuu_cnt(s)))
    i += 1

print(s)
