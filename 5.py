import math
n = 20
n_max = math.factorial(n)
print(n_max)
n_min = n_max

for i in range(2520*19*17*13*11,n_max+1):
    cnt = 0
    for j in range(n):
        if i % (n-j) == 0:
            cnt += 1
        else:
            break
    if cnt == n and n_min > i:
        n_min = i
        break

print(n_min)
