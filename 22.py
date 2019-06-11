alpha = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10,
        'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20,
         'U':21, 'V':22,'W':23, 'X':24, 'Y':25, 'Z':26}

f = open('22.txt', 'r')
data = f.read()
data = data.split(',')
data[-1] = data[-1][:-1]
for i in range(len(data)):
    data[i] = data[i][1:]
    data[i] = data[i][:-1]
data.sort()
score = 0
for i in range(len(data)):
    cnt = 0
    for j in range(len(data[i])):
        cnt += alpha[data[i][j]]
    score += (cnt*(i+1))
    if data[i] == 'COLIN':
        print(cnt*(i+1))
print(score)
        
