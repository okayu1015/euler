sum_c = 1
sum_p = 1
for i in range(10,100): #分子
    for j in range(i+1,100): #分母
        si = str(i)
        sj = str(j)
        if si[0] == sj[1] and (i % 10 != 0 and j % 10 != 0):
            c = int(si[1])
            p = int(sj[0])
            if p / c == j / i:
                print(i)
                print(j)
                sum_c *= i
                sum_p *= j
        elif si[1] == sj[0] and(i % 10 != 0 and j % 10 != 0):
            c = int(si[0])
            p = int(sj[1])
            if p / c == j / i:
                print(i)
                print(j)
                sum_c *= i
                sum_p *= j
            
print(sum_c)
print(sum_p)
