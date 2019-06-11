import math
sum = 0
num = 1001
i = 1
while i < num*num+1:
    if i == 1:
        sum += 1
        i += 2
    elif math.sqrt(i) % 2 == 1: #奇数乗数
        sum += (i + i - (int(math.sqrt(i))-1) +
                i - (int(math.sqrt(i))-1)*2 +
                i - (int(math.sqrt(i))-1)*3)
        i += 2
    else:
        i += 2
print(sum)

