f = open('11.txt', 'r')
data = f.read()
data = data.split('\n')
for i in range(len(data)):
    data[i] = data[i].split()
n_max = 0    
for i in range(len(data) - 4):
    for j in range(len(data[i]) - 3):
        n_sum0 = 1
        n_sum1 = 1
        n_sum2 = 1
        n_sum3 = 1
        for n in range(4):
            n_sum0 *= int(data[i+n][j])
            n_sum1 *= int(data[i][j+n])
            n_sum2 *= int(data[i+n][j+n])
            n_sum3 *= int(data[i+3-n][j+n])
        if n_max < max(n_sum0,n_sum1,n_sum2,n_sum3):
            n_max = max(n_sum0,n_sum1,n_sum2,n_sum3)

print(n_max)
