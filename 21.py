def frnd_lv(num):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum += i
    return sum

print(frnd_lv(220))
print(frnd_lv(frnd_lv(220)))

sum = 0
for i in range(1,10000):
    b = frnd_lv(i)
    a = i
    if frnd_lv(a) == b and frnd_lv(b) == a and b != a:
        print(i)
        sum += i

print(sum)
