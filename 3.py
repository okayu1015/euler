n = 600851475143
i = 3
while n > 1:
    if n % i != 0:
        i += 2
    else:
        print(i)
        n = n / i
        i += 2
        
