p_max = 0
n = 1000
for i in range(1,n):
    for j in range(1,n):
        sum = i*j
        d = str(sum)
        if d == d[::-1]:
            print(d + '=' + str(i) + '*' + str(j))
            if p_max < sum:
                p_max = sum
print(p_max)

