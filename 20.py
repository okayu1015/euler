import math
num = str(math.factorial(100))
ans = 0
for i in range(len(num)):
    ans += int(num[i])
print(ans)
