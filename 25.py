f1 = 1
f2 = 1
f = 0
i = 1
cnt = 2
while len(str(f)) != 1000:
    if i != 1 or i != 2:
        f = f1 + f2
        f1 = f2
        f2 = f
        cnt += 1
    if len(str(f)) == 1000:
        print(f)
        print(cnt)
