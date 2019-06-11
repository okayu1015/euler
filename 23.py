def kajyou(num):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum += i
    if sum > num:
        return num
    else:
        return 0
n = 30
data = [i for i in range(0,n+1)]  

for i in range(1,n+1):
    if kajyou(i) != 0:
        print(i)
