f_sum = 0
sum_f = 0
for i in range(1,100+1):
    f_sum += i**2
    sum_f += i

if f_sum > sum_f**2:
    print(f_sum-sum_f**2)
else:
    print(sum_f**2-f_sum)
