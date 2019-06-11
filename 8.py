f = open('8.txt','r')
data = f.read()
data = data.split('\n')

#リスト連結
for i in range(len(data)-1):
    data[0] += data[i+1]
data = data[0]
print(data)

d_max = 0
n = 13
for i in range(len(data)-n):
    d = 1
    for j in range(n):
        d *=  int(data[i+j])
    if d > d_max:
        d_max = d
print(d_max)
