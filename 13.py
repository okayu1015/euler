f = open('10.txt','r')
data = f.read()
data = data.split()
sum = 0
for i in range(len(data)):
    sum += int(data[i])
sum = str(sum)
print(sum[0:10])
