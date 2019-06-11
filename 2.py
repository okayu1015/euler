a0 = 1
a1 = 2
an = 0
sum = 0
for i in range(4000000):
    print(i)
    if i == 0:
        an = a0
        #print(an)
    elif i == 1:
        an = a1
        #print(an)
    else:
        an = a0 + a1
        a0 = a1
        a1 = an
        #print(an)
    if an % 2 == 0:
        sum += an
    if an > 4000000:
        break
print(sum)
