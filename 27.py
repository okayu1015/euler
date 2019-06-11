import math
#素数判定
def is_prime(n):
    if n == 1: return False
    #for k in range(2, int(math.sqrt(n)) + 1):
    for k in range(2, int(n)):
        if n % k == 0:
            return False

    return True

max = 0
max_ab = 0
cnt = 0
for a in range(-999,1000):
    for b in range(-999,1000):
        for n in range(b+1):
            if is_prime(int(n*n + a*n + b)):
                cnt += 1
        if max < cnt:
            max = cnt
            max_ab = a*b
print(max_ab)
