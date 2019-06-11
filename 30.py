n = (9**5) * 6 
i = 2

while i < n:
    char = str(i)
    sum = 0
    for j in range(len(char)):
        sum += int(char[j])**5
    if sum == i:
        sum_num += i
print(sum_num)
