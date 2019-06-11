num = 100
list = []
for a in range(2,num+1):
    for b in range(2,num+1):
        if a**b not in list:
            list.append(a**b)
print(list)
print(len(list))
