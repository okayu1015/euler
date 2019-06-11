def pita(n):
    for a in range(1,998):
        for b in range(1,988):
            for c in range(1,988):
                if a*a + b*b == c*c and a+b+c == n:
                    return a*b*c
print(pita(1000))
