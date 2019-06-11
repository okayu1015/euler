f = open('18.txt','r')
data = f.read()
data = data.split('\n')
for i in range(len(data)):
    data[i] = data[i].split()
ans = [ [0 for j in range(50)] for i in range(50)]

sum = 3
s = 1
k = 0
for i in range(1,len(data)):
    for j in range(len(data[i])):
        if j != 0 and j != len(data[i])-1:
            ans[i][j] += ((int(data[i-1][j-1]) + int(data[i-1][j])) / 2)
        elif j == 0:
            ans[i][j] += (int(data[i-1][j]) / 2 )
        else:
            ans[i][j] += (int(data[i-1][j-1]) / 2 )
    for j in range(len(data[i])):
        if ans[i][j] == max(ans[i]):
            sum += int(data[i][j])
            break

print(sum)
