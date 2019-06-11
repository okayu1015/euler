import math
for i in range(3,10):
    print(math.factorial(i))

all_sum = 0
for i in range(3,100000):
    s = str(i)
    sn = []
    for k in range(len(s)):
        sn.append(int(s[k]))
    if math.factorial(max(sn)) <= i:
        sum = 0
        for l in range(len(sn)):
            sum += math.factorial(sn[l])
        if sum == i:
            print(i)
            all_sum += i

print(all_sum)
