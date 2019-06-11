n = 11 #n以下の素数の和
print(2)
sum = 2
for i in range(3,n+1,2):
    in_cnt = 0
    for j in range(2,i):
        if i % j == 0:
            in_cnt += 1
            break
    if in_cnt == 0:
        #print(i)
        sum += i

print(sum)
