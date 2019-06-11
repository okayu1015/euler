list = [[5,12,13],[8,15,17],[3,4,5]]
sum_list = [30,40,12]

n = 1
while n <= 1000:
    if n % 30 == 0 and n % 40 ==0 and n % 12 == 0:
        print(n)
    n += 1
