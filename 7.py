cnt = 0
for i in range(3,1000000,2):
    in_cnt = 0
    for j in range(2,i):
        if i % j == 0:
            in_cnt += 1
            break
    if in_cnt == 0:
        cnt += 1
    if cnt >= 10001-1:
        break

print(i)
